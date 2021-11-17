while True:
    print("*" * 25)
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("*" * 25)

    pilihan = int(input("1/2/3/4 : "))

    if pilihan == (int(pilihan)) :
        awal = float(input("Masukan nilai awal : "))
        akhir = float(input("Masukan nilai akhir :"))

        if pilihan == 1:
            print("Anda memilih penjumlahan")
            total = awal + akhir
            print("Hasil dari ",awal," + ",akhir, "adalah :",total)

        elif pilihan == 2:
            print("Anda memilih pengurangan")
            total = awal - akhir
            print("Hasil dari ",awal," - ",akhir, "adalah :",total)

        elif pilihan == 3:
            print("Anda memlihin perkalian")
            total = awal * akhir
            print("Hasil dari ",awal," * ",akhir, "adalah :",total)

        elif pilihan == 4:
            print("Anda memilih pembagian")
            total = awal / akhir
            print("Hasil dari ",awal," / ",akhir, "adalah :",total)

        else:
            print("Pilihan tidak valid")
    else :
        print("Input bukan angka !")
        exit()

    pilihan2 = input("Apakah ingin menghitung lagi?  ketik yes bila hitung lagi : " )
    if pilihan2 ==  "yes":
        continue
    else:
        exit()

    

    













