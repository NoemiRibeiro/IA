# -*- coding: utf-8 -*-
"""
Editor Spyder

"""

from numpy import dot

def função_degrau(x):
    return 1 if x >= 0 else 0

def neurônio_MCP(weights, bias, x):
    vk = dot(weights, x) + bias
    return função_degrau(vk)

x0 = [0,0]
x1 = [0,1]
x2 = [1,0]
x3 = [1,1]

weights = [-1,-1]
bias = 1.5

saida0 = neurônio_MCP(weights, bias, x0)
saida1 = neurônio_MCP(weights, bias, x1)
saida2 = neurônio_MCP(weights, bias, x2)
saida3 = neurônio_MCP(weights, bias, x3)

print("NEURÔNIO MCP IMPLEMENTANDO FUNÇÃO BOOLEANA NAND")
print ("0 NAND 0 = ", saida0)
print ("0 NAND 1 = ", saida1)
print ("1 NAND 0 = ", saida2)
print ("1 NAND 1 = ", saida3)