import math

def sigmoid(x):
    a = -x
    b = math.exp(a)
    c = 1 + b
    d = 1 / c
    return d

def neuronio(inputs, pesos, bias):
    soma = 0
    for i in range(len(inputs)):
        soma += inputs[i] * pesos[i]
    soma += bias
    resultadof = sigmoid(soma) 
    print(resultadof)
    return resultadof

inputs = [1, 2]
pesos = [0.5, 0.5]
bias = 0

neuronio(inputs, pesos, bias)
