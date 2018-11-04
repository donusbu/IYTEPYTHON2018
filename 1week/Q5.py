import math

array_1 = ['5', '2', '8']
print(''.join(array_1))

array_2 = ['7', '0', '1']
print(''.join(array_2))

print(array_1 == array_2)

a = int(''.join(array_1))
b = int(''.join(array_2))
print(a * b)

print(math.sqrt(a * b))
