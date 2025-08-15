file_input="transaksi_kotor.txt"
file_output="laporan_bersih.txt"



try:
    # Membuka file input
    with open(file_input, "r") as f_input:
        # Membuka file output
        with open(file_output, "w") as f_output:
            
            # Tulis header laporan
            f_output.write("LAPORAN TRANSAKSI BERSIH\n")
            f_output.write("=========================\n")
            
            # Variabel untuk menghitung total keseluruhan
            grand_total = 0
            
            # Loop setiap baris
            for baris in f_input:
                baris = baris.strip()  # Bersihkan spasi dan newline
                
                # Lewati baris kosong
                if not baris:
                    continue
                
                # Pecah data menjadi list
                data_potongan = baris.split(",")
                
                # Bersihkan setiap bagian
                id_bersih = data_potongan[0].strip().upper()
                nama_bersih = data_potongan[1].strip().title()
                jumlah = int(data_potongan[2].strip())
                harga_satuan = float(data_potongan[3].strip())
                
                # Hitung total harga
                total_harga = jumlah * harga_satuan
                grand_total += total_harga  # Akumulasi total
                
                # Format dan tulis ke file output
                string_output = (
                    f"ID: {id_bersih} | Produk: {nama_bersih} "
                    f"| Jumlah: {jumlah} | Total Harga: Rp {total_harga}"
                )
            f_output.write(string_output + "\n")
            
            # Footer laporan
            f_output.write("--- ANALISIS SELESAI ---\n")
            f_output.write(f"Total Semua Transaksi: Rp {grand_total}")
    
    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("File transaksi_kotor.txt tidak ditemukan. Pastikan file ada di folder yang sama.")
