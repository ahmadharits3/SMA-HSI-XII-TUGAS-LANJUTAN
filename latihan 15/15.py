

# Membuat dictionary biodata
biodata ={
    "nama" : "ahmad harits",
    "umur" : "18",
    "hobi" : ["mancing","bersepeda"],
    "sudah_menikah" : "false"
}

# Cetak seluruh dictionary
# Cetak value dari key "nama"
# Cetak hobi pertama
print("dictionary:",biodata)
print("nama:",biodata["nama"])
print("hobi pertama:",biodata["hobi"][0])


#latihan 2

# Menambahkan key-value baru
biodata["kota"] = "Jakarta"

# Mengubah umur menjadi umur tahun depan
biodata["umur"] += 1

# Cetak dictionary yang sudah diperbarui
print("Dictionary setelah diperbarui:", biodata)


#latihan 3

# Mengakses key yang tidak ada dengan bracket notation (ini akan error)
# print(biodata["pekerjaan"])  # ← ini akan memunculkan KeyError

# Mengakses key "pekerjaan" dengan .get()
print("Pekerjaan (tanpa default):", biodata.get("pekerjaan"))

# Mengakses key "pekerjaan" dengan default value
print("Pekerjaan (dengan default):", biodata.get("pekerjaan", "Pelajar"))
  


#////////////////////////////////////////////////////////////
pekerjaan=biodata.get("pekerjan")
print(f"pekerjaan :{pekerjaan}")

pekerjaan = biodata.get("pekerjaan", "pelajar")
print(f"Pekerjaan: {pekerjaan}")

#latihan 4

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
print("Histogram kata:", penghitugan)
