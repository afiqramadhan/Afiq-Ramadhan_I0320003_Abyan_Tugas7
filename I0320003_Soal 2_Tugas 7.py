# menampilkan informasi program
print('Progaram Menghitung Banyak Balok Kecil Penyusun Balok Besar')
# input data balok besar
p1 = float(input('Panjang balok besar :'))
l1 = float(input('Lebar balok besar :'))
t1 = float(input('Tinggi balok besar :'))
# input data balok kecil
p2 = float(input('Panjang balok kecil :'))
l2 = float(input('Lebar balok kecil :'))
t2 = float(input('Tinggi balok kecil :'))
# memproses data
v1 = p1*l1*t1
v2 = p2*l2*t2
n = v1/v2
# menampilakn hasil perhitungan
import math
print('Balok besar memiliki volume sebesar', math.ceil(v1))
print('Balok kecil memiliki volume sebesar', math.ceil(v2))
print('Banyak balok kecil penyusun balok besar sebanyak', math.floor(n))
print("Ukuran dimensi 'balok besar' terbesar", max(p1,l1,t1))
print("Ukuran dimensi 'balok kecil' terkecil", min(p2,l2,t2))