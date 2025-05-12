jumlah_mahasiswa = int(input('masukkan jumlah mahasiswa praktikum adp = '))
data_mahasiwa = [ ]
#input data tiap mahasiswa
for i in range (jumlah_mahasiswa) : 
    print(f'mahasiswa ke-{i+1}')
    nama = input('nama = ')
    pretest = float(input('nilai pretest = '))
    posttest = float(input('nilai posttest = '))
    makalah = float(input('nilai makalah = '))

    #nilai akhir
    nilai_akhir = (0.4*pretest)+(0.4*posttest)+(0.2*makalah)
    data_mahasiwa.append([nama,nilai_akhir])

#tabel nilai akhir
print('TABEL NILAI AKHIR MAHASISWA')
print('------------------------------------------')
print('| {:^30} | {:^11} |'.format('Nama Mahasiwa', 'Nilai Akhir'))
print('------------------------------------------')
for mhs in data_mahasiwa : 
    print('| {:^30} | {:^11.2f} |'.format(mhs[0], mhs[1]))
print('------------------------------------------')

#hitung rata rata kelas 
total_nilai = 0 
for mhs in data_mahasiwa :
    total_nilai += mhs[1]
rata_rata = total_nilai/jumlah_mahasiswa
print('rata-rata nilai akhir kelas : {:.2f}'.format(rata_rata))

#nilai tertinggi dan terendah 
nilai_tertinggi = data_mahasiwa[0][1]
nilai_terendah = data_mahasiwa[0][1]
mhs_tertinggi = [data_mahasiwa[0][0]]
mhs_terendah = [data_mahasiwa[0][0]]

for i in range (1, jumlah_mahasiswa) :
    nilai = data_mahasiwa[i][1]
    nama = data_mahasiwa[i][0]

    if nilai > nilai_tertinggi :
        nilai_terendah = nilai 
        mhs_tertinggi = [nama]
    elif nilai == nilai_tertinggi :
        mhs_tertinggi.append(nama)

    if nilai < nilai_terendah : 
        nilai_terendah = nilai
        mhs_terendah = [nama]
    elif nilai == nilai_terendah :
        mhs_terendah.append(nama)
print('nilai tertinggi : {:.2f} oleh'.format(nilai_tertinggi))
for nama in mhs_tertinggi :
    print('-', nama)
print('nilai terendah : {:.2f} oleh'.format(nilai_terendah))
for nama in mhs_terendah :
    print('-', nama)

#daftar nilai mahasiswa di atas rata rata kelas
print('mahasiswa dengan nilai di atas rata-rata kelas : ')
for mhs in data_mahasiwa : 
    if mhs[1] > rata_rata : 
        print('- {}({:.2f})'.format(mhs[0], mhs[1]))
