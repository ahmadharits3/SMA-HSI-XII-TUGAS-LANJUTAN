class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0

    def lihat_saldo(self):
        print(f"Saldo saat ini: Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Berhasil setor Rp{jumlah}. Saldo sekarang: Rp{self.saldo}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi.nabung lagi")
        else:
            self.saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}. Saldo sekarang: Rp{self.saldo}")



# Membuat objek
rekening_budi = RekeningBank("123456", "Budi")
rekening_tsabit=RekeningBank("987654","tsabit_poke")
# Uji coba
# rekening_budi.lihat_saldo()
# rekening_budi.setor(500000)
# rekening_budi.setor(200000)
# rekening_budi.tarik(50000)
# rekening_budi.tarik(50000)
# rekening_budi.lihat_saldo()
print("------------")
rekening_tsabit.lihat_saldo()
rekening_tsabit.setor(200000)
rekening_tsabit.setor(100000)
rekening_tsabit.tarik(10000000)
rekening_tsabit.tarik(500000)
rekening_tsabit.lihat_saldo()

print(f"rekening :{rekening_tsabit.nama_pemilik},no rekening anda:{rekening_tsabit.nomor_rekening},saldo anda :{rekening_tsabit.saldo}")

print("Terimakasih")

