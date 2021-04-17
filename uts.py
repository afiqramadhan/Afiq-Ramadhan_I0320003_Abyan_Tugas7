teks = "The Bourne Identity"
for j in teks.split():
    print(j, end=",")

print('================')
for k in range(4):
    if k==4:
        break
    else:
        print(k)
else:
    print('yes')
print('================')
for k in range(9):
    if k==4:
        break
    else:
        print(k)
else:
    print('yes')
print('================')
numerik = 0.0
delta = -0.1
for p in range(5):
    numerik += delta
    print(numerik)
print('================')
import math as mt
for p in range(3,15,3):
    print(mt.pow(p,2))
print('================')
teks = 'qwert'
for t in teks:
    print(t)
print('================')
teks = 'qwert'
for t in teks[:-2]:
    print(t)
print('================')
teks = 'qwert'
for t in teks[:]:
    print(t)
print('================')
teks = 'qwert'
for t in teks[1:3:1]:
    print(t)
print('================')
teks = 'qwert'
for t in teks[::-2]:
    print(t)