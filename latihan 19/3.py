import re
teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."

match = re.search('python', teks)
print(match.group())  # 'python' → hanya yang pertama

hasil = re.findall('python', teks)
print(hasil)  # ['python', 'python'] → semua kemunculan
