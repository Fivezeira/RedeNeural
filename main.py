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
    return resultadof

def treinar(inputs, pesos, bias, esperado):
    taxa = 0.1
    resultado = neuronio(inputs, pesos, bias)
    erro = esperado - resultado
    for i in range(len(pesos)):
        ajuste = erro * inputs[i] * taxa
        pesos[i] += ajuste


inputs = [1, 2]
esperado = 1
pesos = [0.1, -0.2]
bias = 0

print(neuronio(inputs, pesos, bias))

for i in range(1000):
    treinar(inputs, pesos, bias, esperado)
print(neuronio(inputs, pesos, bias))