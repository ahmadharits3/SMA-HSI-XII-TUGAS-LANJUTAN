belanjaan =[]
belanjaan.append("Telur")          
belanjaan.append("Susu") 
belanjaan.append("Roti")            
belanjaan.insert(0,"Apel")
belanjaan.remove("Susu")
print("hasil belanjaan :",belanjaan)

#latiha 2

nilai = [98, 76, 88, 100, 54]
nilai_urut=sorted() 
print("nilai asli =",nilai)
print("nilai terbaru =",nilai_urut)

#latihan 3

kalimat =input("masukkan kalimat :")
kata_kata =kalimat.split()
kata_kata.sort()
print("banyak kata :", len(kata_kata))
print("kata_terurut:", kata_kata)

#latihan 4

#preiksi skor(a = [1, 20, 3, 4, 5]
#             b = [1, 20, 3, 4, 5]
#             c = [1, 30, 3, 4, 5])


#soal
# a = [1, 2, 3, 4, 5]
# b = a
# c = a.copy()


# b[1] = 20
# c[1] = 30
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")
