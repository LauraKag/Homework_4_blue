# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:54:14 2018

@author: laura
"""

#%%
#Create a function fully_connected to that returns True if a graph is fully connected, False otherwise

graph1={
       "a":["b","c"],
       "b":["d"],
       "c":["d"],
       "d":["e"],
       "e":[],
       }

graph2={
       "a":["b","c"],
       "b":["d"],
       "c":["d"],
       "d":["e"],
       "e":[],
       "f":[]
       }

def fully_connected(graph):
    values=graph.values()
    keys=graph.keys()
    values2=[]
    for i in values:
        for j in i:
            values2.append(j)


    for key in keys:
        nodes=[]
        if key not in values2 and graph[key]==[]:
            nodes.append(key)
    if nodes==[]:
        return True
    else:
        return False
            

fully_connected(graph1)
#%%
fully_connected(graph2)     
    
        
    