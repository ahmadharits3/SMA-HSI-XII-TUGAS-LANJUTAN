try:
    # Membuka file input
    with open("transaksi_kotor.txt", "r", encoding="utf-8") as file_input:
        # Membuka file output
        with open("laporan_bersih.txt", "w", encoding="utf-8") as file_output:
            
            # Tulis header
            file_output.write("LAPORAN TRANSAKSI BERSIH\n")
            file_output.write("=========================\n")
            
            # Variabel untuk total semua transaksi (bonus)
            grand_total = 0
            
            # Membaca setiap baris
            for baris in file_input:
                baris = baris.strip()  # Hapus spasi di awal/akhir
                
                # Lewati baris kosong
                if not baris:
                    continue
                
                # Pecah data jadi list
                data_potongan = baris.split(",")
                
                # Bersihkan setiap bagian
                id_bersih = data_potongan[0].strip().upper()
                nama_bersih = data_potongan[1].strip().title()
                jumlah = int(data_potongan[2].strip())
                harga_satuan = float(data_potongan[3].strip())
                
                # Hitung total harga
                total_harga = jumlah * harga_satuan
                grand_total += total_harga  # akumulasi
                
                # Hanya tulis jika total harga > 500000 (bonus filter)
                if total_harga > 500000:
                    string_output = (
                        f"ID: {id_bersih} | Produk: {nama_bersih} "
                        f"| Jumlah: {jumlah} | Total Harga: Rp {total_harga}"
                    )
                    file_output.write(string_output + "\n")
            
            # Footer + total semua transaksi
            file_output.write(f"--- ANALISIS SELESAI ---\n")
            file_output.write(f"Total Semua Transaksi: Rp {grand_total}")
    
    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("File transaksi_kotor.txt tidak ditemukan. Pastikan file ada di folder yang sama.")
