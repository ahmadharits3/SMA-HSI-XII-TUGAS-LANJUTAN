import re
nomor = input("Masukkan nomor telepon: ")

if re.search(r'^\d+$', nomor) and 10 <= len(nomor) <= 13:
    print("Format nomor telepon valid.")
else:
    print("Format tidak valid.")
