# Demostración de igualdad entre expresiones (BASE CANÓNICA) en el plano

a , b = 3 , 5

vector_u = [ a , b ]

#base_canonica = a * [1 , 0] + b * [0 , 1]
base_canonica = [ x + y for x , y in zip( [ x * a for x in [1 , 0] ],[ x * b for x in [0 , 1]  ]) ]

print(vector_u == base_canonica)
