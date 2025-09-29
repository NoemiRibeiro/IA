# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 19:58:29 2025

@author: Noêmi Ribeiro
"""
from numpy import dot

def função_degrau(x):
    return 1 if x >= 0 else 0

def neurônio_MCP(pesos, entradas):
    uk = dot(pesos, entradas)
    return função_degrau(uk)

def feed_forward(rede_xor, vetor_entrada):
    """ recebe uma rede neural (representada como uma lista de listas de listas 
    de pesos) e retorna a saída da propagação direta da entrada """
    
    vetor_saída = []
    
    for ponteiro in rede_xor:
        
        entrada_com_bias = vetor_entrada + [1]              # adiciona bias ao vetor de entrada
        saída = [neurônio_MCP(neurônio, entrada_com_bias)   # calcula a saída
                 for neurônio in ponteiro]                  # para a camada de rede
        vetor_saída.append(saída)                           # adiciona ao vetor de saída
        
        # a entrada para a próxima camada é a saída desta etapa
        vetor_entrada = saída
        
    return vetor_saída

sinapses_xor = [#camada oculta
               [[1, 1, -1.5],  # neurônio AND
                [1, 1, -0.5]], # neurônio OR
               # camada de saída
               [[-2, 1, -0.5]]] # neurônio = segunda entrada
                                # menos a primeira entrada
                                
for x in [0,1]:
    for y in [0,1]:
        print (x," EXCLUSIVO ", y, " = ", feed_forward(sinapses_xor, [x,y])[-1])