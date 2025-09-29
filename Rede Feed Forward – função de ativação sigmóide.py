# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 20:17:17 2025

@author: Noêmi Ribeiro
"""

from numpy import dot
import math

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neurônio_MCP(pesos, entradas):
    uk = dot(pesos, entradas)
    return sigmoid(uk)

def feed_forward(rede_xor, vetor_entrada):
    """ recebe uma rede neural (representada como uma lista de listas de listas 
    de pesos) e retorna a saída da propagação direta da entrada """
    
    vetor_saída = []
    
    for ponteiro in rede_xor:
        
        entrada_com_bias = vetor_entrada + [1]             # adiciona bias ao vetor de entrada
        saída = [neurônio_MCP(neurônio, entrada_com_bias)  # calcula a saída
                 for neurônio in ponteiro]                 # para a camada de rede
        vetor_saída.append(saída)                          # adiciona ao vetor de saída
        
        # a entrada para a próxima camada é a saída desta etapa
        vetor_entrada = saída
        
    return vetor_saída

sinapses_xor = [ # camada oculta
                [[20, 20, -30],   # neurônio AND
                 [20, 20, -10]],  # neurônio OR
                # camada de saída
                [[-60, 60, -30]]] # neurônio = segunda entrada
                                  # menos a primeira entrada

for x in [0,1]:
    for y in [0,1]:
        print (x, " EXCLUSIVO ", y, " = ", feed_forward(sinapses_xor, [x,y])[-1])