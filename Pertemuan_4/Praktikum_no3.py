cx, cy = map(int, input().split())
T_awal_x, T_awal_y =  map(int, input().split())
T_akhir_x, T_akhir_y =  map(int, input().split())

jarak = ((T_akhir_x - T_awal_x)**2 + (T_akhir_y - T_awal_y)**2)**0.5

j_akhir_kelingkaran = ((T_akhir_x - cx)**2 + (T_akhir_y - cy)**2)**0.5

Time_to_end = jarak

if j_akhir_kelingkaran > Time_to_end :
    print("Yes")
else:
    print("No")