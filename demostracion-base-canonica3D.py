# Demostración de igualdad entre expresiones (BASE CANÓNICA) en el espacio

"""
Todos los vectores pueden ser representados como la suma de otros vectores

por ejemplo el vector_u = (a , b , c) puede ser expresado como la suma de (a * i) + (b * j) + (c * k)

siendo los vectores i , j , k unitarios de componentes constantes

i = [1 , 0, 0]
j = [0 , 1, 0]
k = [0 , 0, 1]

"""

a , b, c = 3 , 2, -4

vector_u = [ a , b , c ]

v_i = [1 , 0, 0] # Unitario i
v_j = [0 , 1, 0] # Unitario j
v_k = [0 , 0, 1] # Unitario k


#base_canonica = a * [1 , 0, 0] + b * [0 , 1, 0] + c * [0 , 0, 1]
#base_canonica = a * v_i + b * v_j * v_k
base_canonica = [ x + y + z for x , y, z in zip( [ x * a for x in v_i ],[ y * b for y in v_j ], [ z * c for z in v_k ] ) ]


print(vector_u == base_canonica)
