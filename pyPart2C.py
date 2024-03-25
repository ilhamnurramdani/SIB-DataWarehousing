# B. Jumlah Kuadrat:
# Buat Function yang menghitung jumlah kuadrat dari semua bilangan dari 1 hingga bilangan tertentu n.

# penyelesain 1
def kuadrat(n):
    angka =  0
    for i in range(1, n+1):
        i = i**2
        angka +=1
        print(f"jumlah kuadrat dari angka {angka} adalah: {i}")

bilangan = int(input("Masukan Bilangan :"))
kuadrat(bilangan)

# #penyelesain 2
def kuadrat2(n):
    hasil =  0
    for i in range(1, n+1):
        hasil += i**2
    print("jumlah kuadrat dari",n,"adalah:",hasil)

bilangan2 = int(input("Masukan Bilangan :"))
kuadrat2(bilangan2)

# C. Perhitungan Faktorial:
# Buat Function yang menghitung faktorial dari sebuah bilangan tertentu.

def faktorial(bilangan):
    jumlah = 1
    for i in range(1, bilangan+1):
        jumlah *= i
    print(jumlah)
angka = int(input("Masukan angka :"))
faktorial(angka)

# D. Barisan Fibonacci:
# Buat Function untuk menghasilkan barisan Fibonacci hingga sejumlah bilangan tertentu yang ditentukan oleh pengguna.

def fibonacci(n):
    a, b = 0,1
    for i in range(1, n+1):
        c = a+b
        a = b
        b = c
        print(c)

angkaF = int(input("Masukan Angka :"))
fibonacci(angkaF)

# E. Fungsi Penghitung Gaji:
# Buatlah sebuah program untuk menghitung gaji karyawan berdasarkan jumlah jam kerja dan tarif per jam. Program harus menggunakan sebuah fungsi yang menerima jumlah jam kerja dan tarif per jam sebagai argumen, dan mengembalikan jumlah gaji karyawan.

def hitungGaji(gaji, jam):
    jumlahGajiKaryawan = gaji * jam
    return jumlahGajiKaryawan

gaji = int(input('Masukan Gaji :'))
jam = int(input('Masukan Jumlah Jam Kerja:'))
jumlahGajiKaryawan = hitungGaji(gaji, jam)
print(f"Jumlah Gaji : {jumlahGajiKaryawan}")

# F. Fungsi Pengecekan Bilangan Prima:
# Buatlah sebuah program untuk memeriksa apakah sebuah bilangan yang dimasukkan oleh pengguna adalah bilangan prima atau bukan. Program harus menggunakan sebuah fungsi yang menerima bilangan sebagai argumen, dan mengembalikan nilai True jika bilangan tersebut prima, dan False jika tidak.

def bilPrima(bilangan):
    if(bilangan <= 1):
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0 :
            return False
    return True

bilanganPrima = int(input("Masukan Bilangan :"))
print(bilPrima(bilanganPrima))


    