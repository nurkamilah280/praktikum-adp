print("=== Kalkulator Matriks ===")

ulang = "y"
while ulang == "y":
    print("\nMasukkan matriks A:")
    baris_A = int(input("Jumlah baris A: "))
    kolom_A = int(input("Jumlah kolom A: "))
    matriks_A = []
    for i in range(baris_A):
        baris = []
        for j in range(kolom_A):
            elemen = int(input("A[" + str(i) + "][" + str(j) + "]: "))
            baris.append(elemen)
        matriks_A.append(baris)

    print("\nMasukkan matriks B:")
    baris_B = int(input("Jumlah baris B: "))
    kolom_B = int(input("Jumlah kolom B: "))
    matriks_B = []
    for i in range(baris_B):
        baris = []
        for j in range(kolom_B):
            elemen = int(input("B[" + str(i) + "][" + str(j) + "]: "))
            baris.append(elemen)
        matriks_B.append(baris)

    selesai = False
    while not selesai:
        print("\n=== Menu Operasi ===")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Matriks")
        print("4. Transpose Matriks")
        print("5. Determinan Matriks")
        print("6. Invers Matriks")
        print("0. Keluar")

        pilihan = input("Pilih operasi (0-6): ")

        if pilihan == "1":
            if baris_A == baris_B and kolom_A == kolom_B:
                print("Hasil A + B:")
                for i in range(baris_A):
                    for j in range(kolom_A):
                        print(matriks_A[i][j] + matriks_B[i][j], end=" ")
                    print()
            else:
                print("Ukuran matriks tidak sama!")

        elif pilihan == "2":
            if baris_A == baris_B and kolom_A == kolom_B:
                print("Hasil A - B:")
                for i in range(baris_A):
                    for j in range(kolom_A):
                        print(matriks_A[i][j] - matriks_B[i][j], end=" ")
                    print()
            else:
                print("Ukuran matriks tidak sama!")

        elif pilihan == "3":
            if kolom_A == baris_B:
                print("Hasil A x B:")
                for i in range(baris_A):
                    for j in range(kolom_B):
                        jumlah = 0
                        for k in range(kolom_A):
                            jumlah += matriks_A[i][k] * matriks_B[k][j]
                        print(jumlah, end=" ")
                    print()
            else:
                print("Kolom A harus sama dengan baris B!")

        elif pilihan == "4":
            print("Transpose A:")
            for i in range(kolom_A):
                for j in range(baris_A):
                    print(matriks_A[j][i], end=" ")
                print()
            print("Transpose B:")
            for i in range(kolom_B):
                for j in range(baris_B):
                    print(matriks_B[j][i], end=" ")
                print()

        elif pilihan == "5":
            pilih_matriks = input("Pilih matriks (A/B): ").upper()
            if pilih_matriks == "A":
                matriks = matriks_A
                baris = baris_A
                kolom = kolom_A
            elif pilih_matriks == "B":
                matriks = matriks_B
                baris = baris_B
                kolom = kolom_B
            else:
                print("Pilihan tidak valid")
                continue

            if baris == kolom:
                if baris == 2:
                    a = matriks[0][0]
                    b = matriks[0][1]
                    c = matriks[1][0]
                    d = matriks[1][1]
                    det = a * d - b * c
                    print("Determinan matriks", pilih_matriks + ":", det)
                elif baris == 3:
                    a = matriks[0][0]
                    b = matriks[0][1]
                    c = matriks[0][2]
                    d = matriks[1][0]
                    e = matriks[1][1]
                    f = matriks[1][2]
                    g = matriks[2][0]
                    h = matriks[2][1]
                    i = matriks[2][2]
                    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
                    print("Determinan matriks", pilih_matriks + ":", det)
                else:
                    print("Hanya mendukung 2x2 dan 3x3")
            else:
                print("Matriks bukan matriks persegi!")

        elif pilihan == "6":
            pilih_matriks = input("Pilih matriks (A/B): ").upper()
            if pilih_matriks == "A":
                matriks = matriks_A
                baris = baris_A
                kolom = kolom_A
            elif pilih_matriks == "B":
                matriks = matriks_B
                baris = baris_B
                kolom = kolom_B
            else:
                print("Pilihan tidak valid")
                continue

            if baris == kolom:
                if baris == 2:
                    a = matriks[0][0]
                    b = matriks[0][1]
                    c = matriks[1][0]
                    d = matriks[1][1]
                    det = a * d - b * c
                    if det == 0:
                        print("Matriks tidak memiliki invers!")
                    else:
                        print("Invers matriks", pilih_matriks + ":")
                        print(d / det, -b / det)
                        print(-c / det, a / det)
                elif baris == 3:
                    a = matriks
                    det = (
                        a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
                        - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0])
                        + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0])
                    )
                    if det == 0:
                        print("Matriks tidak memiliki invers!")
                    else:
                        print("Invers matriks", pilih_matriks + ":")
                        invers = []
                        for i in range(3):
                            baris_baru = []
                            for j in range(3):
                                m1 = (i+1)%3
                                m2 = (i+2)%3
                                n1 = (j+1)%3
                                n2 = (j+2)%3
                                kof = (a[m1][n1]*a[m2][n2] - a[m1][n2]*a[m2][n1])
                                if (i + j) % 2 == 1:
                                    kof = -kof
                                baris_baru.append(kof / det)
                            invers.append(baris_baru)
                        for j in range(3):
                            for i in range(3):
                                print(round(invers[i][j], 2), end=" ")
                            print()
                else:
                    print("Hanya mendukung 2x2 dan 3x3")
            else:
                print("Matriks bukan persegi!")

        elif pilihan == "0":
            selesai = True
        else:
            print("Pilihan tidak valid!")

    ulang = input("\nIngin coba lagi dengan matriks baru? (y/t): ")

print("Terima kasih sudah menggunakan kalkulator matriks!")
