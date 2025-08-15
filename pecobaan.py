# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Ubah ke lowercase
kalimat = kalimat.lower()

# Pisahkan menjadi list kata
kata_kata = kalimat.split()

# Buat dictionary untuk histogram
penghitugan = {}

for kata in kata_kata:
    # Cara aman dan ringkas menggunakan .get()
    penghitugan[kata] = penghitugan.get(kata, 0) + 1

# Cetak hasil histogram
print("hasih penghitunang:", penghitugan)
