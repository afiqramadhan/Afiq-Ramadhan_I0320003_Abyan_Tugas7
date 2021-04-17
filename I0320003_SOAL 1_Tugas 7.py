# menampilkan informasi program
judul = "Reservasi Tempat Ngabuburit"
x = judul.center(40,'~')  #metode center
y = x.upper() #metode upper untuk menghasilkan teks kapital
print(y)
nama = input("Masukkan Nama Anda : ")
z = nama.capitalize() #metode capitalize
date = str(input("Masukkan Tanggal Acara: "))
time = str(input("Masukkan Jam Acara: "))
jmlh = int(input("Masukkan Jumlah Partisipan: "))
no = str(input("Masukkan Nomor Telepon Anda: "))
print('Paket yang Tersedia selama Ramadhan:')
print('>> A. Paket Keluarga')
print('>>>>> Keterangan: ')
print('>>>>> 1.Partisipan sebanyak 2-5 orang')
print('>>>>> 2.Wajib melakukan DP 50%')
print('>>>>> 3.Menu Prasmanan')
print('>> B. Paket Teman')
print('>>>>> Keterangan:')
print('>>>>> 1.Partisipan minimal 7 orang')
print('>>>>> 2.Wajib melakukan DP 25%')
print('>>>>> 3.Menu makanan paket dapat disesuaikan selera')
print('>>>>> 4.Biaya termasuk hiburan')
paket = input('Masukkan Paket yang Anda Pilih: ')
if paket == 'A' or 'a':
    dp = 0.5*jmlh*25000
elif paket == 'B' or 'b':
    dp = 0.25*jmlh*25000
print('Terima Kasih Tuan/Nyonya',z)
print('\n=============================================')
print('Berikut kami sampaikan pesanan atas nama', z)
print('Reservasi pada tanggal', date)
print('Reservasi Pukul', time)
print('Paket yang dipilih adalah paket', paket)
print('Partisipan sebanyak', jmlh)
print('DP sebesar ', dp)
print('=============================================')
print('Untuk selebihnya akan kami hubungi via telepon ke nomor',no)