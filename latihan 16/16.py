harga_buah = {"apel": 5000, "jeruk": 8500, "mangga":7800, "pisang": 3000}

total=0
for nama, harga in harga_buah.items():
    print(f"buah {nama} 1kg harganya {harga}.")
    total+= harga

print(f"harga total semua: Rp {total}")

#latihan 2

# Dictionary kosong
kontak = {}

# Menambahkan tiga kontak
kontak["Ibu"] = "081234567890"
kontak["Ayah"] = "089876543210"
kontak["Teman"] = "082233445566"

# Ubah nomor telepon "Ibu"
kontak["Ibu"] = "081298765432"

# Hapus kontak "Teman" menggunakan .pop()
kontak.pop("Teman")

# Cetak dictionary kontak akhir
print("Kontak akhir:", kontak)


# latihan 3

# Nested dictionary untuk produk
produk = {
    "PROD001": {"nama": "Laptop Gaming", "harga": 15000000, "stok": 5},
    "PROD002": {"nama": "Mouse Wireless", "harga": 250000, "stok": 20}
}

# Cetak nama dan harga produk dengan ID PROD002
print(f"Nama: {produk['PROD002']['nama']}")
print(f"Harga: Rp {produk['PROD002']['harga']}")


#latihan 4

# Membaca file mbox-short.txt dan menghitung frekuensi hari
frekuensi_hari = {}

with open("mbox-short.txt", "r") as file:
    for baris in file:
        if baris.startswith("From "):
            kata = baris.split()
            hari = kata[2]  # kata ketiga adalah hari
            frekuensi_hari[hari] = frekuensi_hari.get(hari, 0) + 1

print(frekuensi_hari)
