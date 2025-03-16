print('>>>>>>>>> SELAMAT DATANG <<<<<<<<<')
pemain_1 = input('pemain 1 : ')
pemain_2 = input('pemain 2 : ')
print(pemain_1, 'Vs', pemain_2)
print('pemain 1 :', pemain_1)
n = int(input('masukkan batas angka positif : '))
k = int(input('pilih angka BOM              : '))
for i in range (1, n+1) :
    if i % k == 0 :
        print('BOM', end =' ')
    else :
        print(i, end =' ') 
       
print('pemain 2 :', pemain_2)
m = int(input('tebak angka positif : '))
while m > n :
    print('angka yang anda masukkan melebihi batas rentang angka')
    m = int(input('tebak ulang : '))
if m % k == 0 :
    print( 'angka', m, 'adalah angka BOM', pemain_2,'anda kalah !')
else : 
    print('angka', m, 'bukan angka BOM, selamat', pemain_1,'anda menang!')

            
