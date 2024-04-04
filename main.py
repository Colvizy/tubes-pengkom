print ('SELAMAT DATANG')
print ('SILAHKAN PILIH PRODUK YANG DIINGINKAN')
baris1 = '| A | B | C | D | E |'
baris2 = '| F | G | H | I | J |'
baris3 = '| K | L | M | N | O |'
print (baris1)
print (baris2)
print (baris3)

Baris1 = [0 for i in range (5)]
Baris2 = [0 for i in range (5)]
Baris3 = [0 for i in range (5)]
i = 0

import random
harga = [5,10,15,20,25,30,35,40]
produk = ['spion','bohlam','kampas rem','cakram rem','handgrip','tuas rem dan kopling','filter udara','oli', 'busi', 'rantai']
random.shuffle(harga)
random.shuffle(produk)

for char in baris1:
    if (char == '|' or char == ' '):
        i = i
    else:
        Baris1[i] = char
        i = i + 1
i = 0        
for char in baris2:
    if (char == '|' or char == ' '):
        i = i
    else:
        Baris2[i] = char
        i = i + 1
i = 0        
for char in baris3:
    if (char == '|' or char == ' '):
        i = i
    else:
        Baris3[i] = char
        i = i + 1        
pilih = str(input('Masukkan pilihan produk anda: '))
def beli (pilih):
    i = 0
    while (i <= 5):
        if (Baris1[i] == pilih):
            print ('Anda memilih produk: ' +str(Baris1[i]))
            break
        elif (Baris2[i] == pilih):
            print ('Anda memilih produk: ' +str(Baris2[i]))
            break
        elif (Baris3[i] == pilih):
            print ('Anda memilih produk: ' +str(Baris3[i]))
            break
        else:
            i = i+1
    print ('Produk ' +str(pilih) + ' adalah sebuah ' +str(produk[i])+' dengan harga '+str(harga[i])+ ' ribu rupiah')
    lanjut = str(input('Apakah anda ingin melanjutkan transaksi? (ketik YA/TIDAK) '))
    if (lanjut == 'YA'):
        print ('Silahkan lakukan pembayaran dan selamat menikmati barang anda')
    else:
        lanjut2 = str(input('Apakah anda ingin membatalkan pembelian atau memilih produk lain? (ketik BATAL/PILIH) '))
        if (lanjut2 == 'BATAL'):
            print ('Sampai bertemu kembali')
        else:
            print ('\033c', end='')
            print ('SELAMAT DATANG')
            print ('SILAHKAN PILIH PRODUK YANG DIINGINKAN')
            print (baris1)
            print (baris2)
            print (baris3)
            pilih1 = str(input('Masukkan pilihan produk anda: '))
            beli(pilih1)
            
beli(pilih)            

