#latihan 1

jadwal_senin =["Matematika", "Bahasa Indonesia", "Olahraga", "Sejarah"]
print("jadwal hari senin adalah :",jadwal_senin)
print(f"mapel pertama yaitu: {jadwal_senin[0]}")
print(f"pelajaran terakhir yaitu: {jadwal_senin[-1]}")

#latiha 2

jadwal_senin[2]= "Kimia"
print("jadwal terbaru :",jadwal_senin)

#latihan 3

nilai_mentah =  [55, 63, 72, 81, 90]
for i in range(len(nilai_mentah)) :
    nilai_mentah[i] += 5

print("nilai terbaru",nilai_mentah)

#latihan 4


awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu =["Kamis", "Jumat", "Sabtu", "Minggu"]

seminggu =awal_minggu + akhir_minggu
hari_kerja =seminggu[0:5]
print(hari_kerja_aktive)