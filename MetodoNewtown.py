import math

#metod de newton- raphson
#import numpy as np

#defino la funcion
fx = lambda x: x**3 + 4*(x**2) -10
#degino la derivada de la funcion
dfx = lambda x: 3*(x**2)
#punto de partida
x0 = 2
#criterio de parada con margen de error
tolerancia = 0.0001

# formula de newton- raphson
def newton_method(f, f_prime, x0, epsilon):
    xi = x0
    tramo = abs(2*tolerancia)
    while not (tramo<=tolerancia):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo = abs (xnuevo - xi)
        xi = xnuevo
    return xi


print ('valor xnuevo : ')
print (xnuevo)
print ('valor tramo : ')
print (tramo)



