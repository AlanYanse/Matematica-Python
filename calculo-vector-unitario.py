
import math


"""
El vector unitario es un vector que tiene un modulo de |1| 
Para calcular el unitario de un determinado vector hay que dividir al vector sobre su modulo

"""

vector = [-2,6]

def modulo(vector):
    """
    vector -> k
    retorna el modulo del vector ingresado por parametro
    """
    modulo = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    return modulo

def unitario(vector , modulo):
    """
    (vector, k) -> vector
    retorna el vector unitario correspondiente al vector ingresado por parametro
    """
    unitario = [vector[0] / modulo , vector[1] / modulo]
    return unitario

print(unitario(vector,modulo(vector)))












