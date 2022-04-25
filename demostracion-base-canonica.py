# Demostración de igualdad entre expresiones (BASE CANÓNICA) en el plano

a , b = 3 , 5

vector_u = [ a , b ]

v_i = [1 , 0] # Unitario i
v_j = [0 , 1] # Unitario j


#base_canonica = a * [1 , 0] + b * [0 , 1]
#base_canonica = a * v_i + b * v_j
base_canonica = [ x + y for x , y in zip( [ x * a for x in v_i ],[ x * b for x in v_j ]) ]

print(vector_u == base_canonica)
