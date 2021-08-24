# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('======== lebih dari (>) ==========')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari dari <
print('======== kurang dari (<) ==========')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# kurang dari dari >=
print('======== lebih dari sama dengan (>=) ==========')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# kurang dari dari >=
print('======== kurang dari sama dengan (<=) ==========')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan (==)
print('======== sama dengan (==) ==========')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# tidaksama dengan (!=)
print('======== sama dengan (!=) ==========')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# 'is' sebagai komparasi object identity
print('======== object identiti (is) ==========')
x = 5  # ini adalah assignment membuat object
y = 5
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5  # ini adalah assignment membuat object
y = 6
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)


print('======== object identiti (is not) ==========')
x = 5  # ini adalah assignment membuat object
y = 5
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is y =', hasil)

x = 5  # ini adalah assignment membuat object
y = 6
print('nilai x =', x, ', id = ', hex(id(x)))
print('nilai y =', y, ', id = ', hex(id(y)))
hasil = x is not y
print('x is y =', hasil)
