# Даны две целые переменные a, b. Составьте фрагмент программы, 
# после исполнения которого значения переменных поменялись бы местами 
# (новое значение a равно старому значению b и наоборот)


a = 1
b = 2

t = a
a = b
b = t

assert(a == 2)
assert(b == 1)

print('result:', a, b)