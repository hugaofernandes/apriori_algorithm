
# -*- coding: utf-8 -*-

from itertools import combinations
import numpy as np
import pandas as pd
import random


def apriori(data, support, minlen, confianca):
    ts = pd.get_dummies(data.unstack().dropna()).groupby(level=1).sum()
    collen, rowlen = ts.shape
    pattern = []
    iterations = 0
    for cnum in range(minlen, rowlen+1):
        for cols in combinations(ts, cnum):
            patsup = ts[list(cols)].all(axis=1).sum()
            a = patsup
            patsup = float(patsup)/collen
            aux = list(cols)
            del aux[-1]
            confiance = 0
            b = ts[aux].all(axis=1).sum()
            if b != 0:
                confiance = float(a)/b
            pattern.append([",".join(cols), patsup*100, confiance*100])
            iterations += 1
    sdf = pd.DataFrame(pattern, columns=["Padrao", "Suporte", "Confianca"])
    results = sdf[sdf.Suporte >= support]
    results = results[results.Confianca >= confianca]
    print (results)
    print ('Iterações: ' + str(iterations))

def legsFunction(legs, n, s):
	if legs == n:
		return s
	return np.nan

####################### zoo ##########################

zoo = pd.read_csv('zooOriginal.csv', sep=',', header=None)
zoo.columns = ['name','hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','legs','tail','domestic','catsize','type']
zoo = zoo.drop(['name'], axis=1)
zoo = zoo.drop(['type'], axis=1)
legs = zoo['legs']
zoo = zoo.drop(['legs'], axis=1)
for i in list(zoo.columns.values):
	zoo[i] = zoo[i].replace(1, i)
	zoo[i] = zoo[i].replace(0, np.nan)
zoo['No Legs'] = legs.apply(lambda x : legsFunction(x, 0, 'No Legs'))
zoo['2 Legs'] = legs.apply(lambda x : legsFunction(x, 2, '2 Legs'))
zoo['4 Legs'] = legs.apply(lambda x : legsFunction(x, 4, '4 Legs'))
zoo['5 Legs'] = legs.apply(lambda x : legsFunction(x, 5, '5 Legs'))
zoo['6 Legs'] = legs.apply(lambda x : legsFunction(x, 6, '6 Legs'))
zoo['8 Legs'] = legs.apply(lambda x : legsFunction(x, 8, '8 Legs'))

#print (zoo)

apriori(zoo, 30, 4, 97)


###################### transations ###################

#transations = pd.read_csv('transations.csv',sep=',')

#print (transations)

#apriori(transations, 30, 4, 97)







