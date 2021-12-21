import numpy as np

a = 5
b = 6   

print(a*b)

for i in range(0, b):
    print(i)

random = np.random.randint(10, size=1)

print(f'El número aleatorio es {random}')

print(f'El número aleatorio al cuadrado es {random**2}')

print(f'El número aleatorio al cubo es {random**3}')