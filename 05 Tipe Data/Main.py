# a = 10, a adalah variabel dengan nilai 10


# tipe data: Angka satuan (integer)
from ctypes import c_double
data_integer = 10000
data_integer = 5
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: fload
data_float = 1.5
print(data_float)
print("- bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup 20"
print(data_float)
print("- bertipe : ", type(data_string))

# tipe data: biner true/fals (boolean)
data_bool = False
print(data_float)
print("- bertipe : ", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print(data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari bahasa C

data_c_double = c_double(10.5)
print(data_c_double)
print("- bertipe : ", type(data_c_double))
