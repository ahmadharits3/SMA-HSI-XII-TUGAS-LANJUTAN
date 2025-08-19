# Latihan 4: Dictionary dengan Tuple Key
papan_catur = {}
papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(1, 'b')] = "Kuda Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"
papan_catur[(8, 'g')] = "Kuda Hitam"

print("Isi papan catur:", papan_catur)
print("Bidak di posisi (1, 'a'):", papan_catur[(1, 'a')])