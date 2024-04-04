sukuCadang = ['Spion', 'Bohlam', 'Kampas rem', 'Cakram rem', 'Handgrip', 'Tuas rem dan kopling', 'Filter udara', 'Oli', 'Busi', 'Rantai']
harga = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
looping = True
stock = [2, 3, 5, 9, 2, 0, 8, 9, 10, 0]

while(looping == True):
    print("Welcome to Vending Machine Sparepart for Vehicle!")
    print("Silahkan pilih sparepart yang ingin dibeli.")
    print('| 1 | 2 | 3 | 4 | 5 |')
    print('| 6 | 7 | 8 | 9 | 10 |')
    print()
    print("Keterangan: ")
    print("1. Spion           6. Tuas rem dan kopling\n2. Bohlam          7. Filter udara \n3. Kampas rem      8. Oli \n4. Cakram rem      9. Busi \n5. Handgrip       10. Rantai")
    print()
    pilihan = int(input("Pilihan yang ingin anda beli (1-10): "))
    pilihan -= 1 # Karena array mulai dari 0
    print()

    if(stock[pilihan] == 0):
        print("Sayang sekali, stock suku cadang yang anda inginkan sudah habis.")
        print("Apakah anda ingin membeli barang lain?")
        pilihan_lanjut = input("Pilihan (Y/N): ")
        if(pilihan_lanjut == "N"):
            looping = False

    else:
        konfirmasi = input(f"Apakah anda ingin membeli {sukuCadang[pilihan]} dengan harga Rp {harga[pilihan]} rupiah?\nPilihan (Y/N): ")
        if(konfirmasi == 'Y'):
            print()
            metodePembayaran = int(input("Pilih metode pembayaran: \n1. Uang Tunai/Cash \n2. Kartu kredit \nPilihan (1/2): "))
            print()
            if(metodePembayaran == 1):
                cash = int(input("Masukkan cash yang tersedia: "))
                if(cash < harga[pilihan]):
                    print(f"Uang kamu kurang {abs(cash-harga[pilihan])}")
                    print()
                    print("Apakah anda ingin membeli barang lain?")
                    pilihan_lanjut = input("Pilihan (Y/N): ")
                    if(pilihan_lanjut == "N"):
                        looping = False
                
                else:
                    stock[pilihan] = stock[pilihan] - 1
                    print("Terima kasih telah bertransaksi dengan kami.")
                    print(f"Jumlah sekarang {sukuCadang[pilihan]}: {stock[pilihan]}")
                    if(cash > harga[pilihan]):
                        print(f"Kembalian anda: {cash-harga[pilihan]}")
                    print()
                    print("Apakah anda ingin membeli barang lain?")
                    pilihan_lanjut = input("Pilihan (Y/N): ")
                    if(pilihan_lanjut == "N"):
                        looping = False

            else:
                kartu_kredit = int(input("Masukkan kartu kredit anda: "))
                stock[pilihan] = stock[pilihan] - 1
                print("Terima kasih telah bertransaksi dengan kami.")
                print(f"Jumlah sekarang {sukuCadang[pilihan]}: {stock[pilihan]}")
                print()
                print("Apakah anda ingin membeli barang lain?")
                pilihan_lanjut = input("Pilihan (Y/N): ")
                if(pilihan_lanjut == "N"):
                        looping = False

print()
print("Terima kasih telah berbelanja! :)")





