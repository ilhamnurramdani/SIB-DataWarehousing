# soal 1

angka = int(input('Masukan angka :'))

if (angka % 2 == 0) :
    print(f"{angka} adalah Bilangan Genap")
else :
    print(f"{angka} adalah Bilangan Ganjil")


# #soal 2

nilaiSiswa = int(input('Masukan Nilai :'))

if(nilaiSiswa >= 70):
    print("Lulus")
else:
    print("Tidak Lulus")
    

# #soal 3
nilai = int(input('Masukan Nilai :'))

if(nilai >= 80 and nilai <= 100) :
    kategori = 'A'
elif(nilai >= 60 and nilai <= 79 ):
    kategori = 'B'
elif(nilai >= 40 and nilai <= 59 ):
    kategori = 'C'
else :
    kategori = 'D'
    
print(kategori)

#soal 4 
kehadiran = int(input('Kehadiran :'))
tugas = int(input('Tugas :'))
kuis = int(input('kuis :'))
UTS = int(input('UTS :'))
UAS = int(input('UAS :'))

nilaiAkhir = (kehadiran * 0.1) + (tugas * 0.2) + (kuis * 0.2) + (UTS * 0.25) + (UAS * 0.25)
if(nilaiAkhir >= 80) :
    predikat = "A"
elif (nilaiAkhir >= 70 and nilaiAkhir <80):
    predikat = "B"
elif(nilaiAkhir >= 60 and nilaiAkhir <70):
    predikat = "C"
elif(nilaiAkhir >= 50 and nilaiAkhir < 60):
    predikat = "D"
else :
    predikat = "E"

print(f"Nilai Akhir anda : {nilaiAkhir}")
print(f"Predikat Anda : {predikat}")

#soal 5

tahun = int(input("Masukan Tahun :"))

if(tahun % 4 == 0 and tahun % 100 != 0 and tahun % 400 != 0) :
    print("tahun kabisat")
else:
    print("Bukan Tahun Kabisat")


