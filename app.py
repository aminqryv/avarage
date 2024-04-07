def hesapla_ortalama(ders_adi, ballar):
    ballarin_cemi = sum(ballar)
    ortalama = ballarin_cemi / len(ballar)
    return ders_adi, ortalama

ders1 = input("Ders 1 Adı: ")
ballar1 = [float(input(f"{ders1} Puan {i+1}: ")) for i in range(3)]
ders2 = input("Ders 2 Adı: ")
ballar2 = [float(input(f"{ders2} Puan {i+1}: ")) for i in range(3)]
ders3 = input("Ders 3 Adı: ")
ballar3 = [float(input(f"{ders3} Puan {i+1}: ")) for i in range(3)]

ders_1_ortalama = hesapla_ortalama(ders1, ballar1)
ders_2_ortalama = hesapla_ortalama(ders2, ballar2)
ders_3_ortalama = hesapla_ortalama(ders3, ballar3)
print("---------------------------------------------")
print(f"{ders_1_ortalama[0]} Ortalama: {ders_1_ortalama[1]:.2f}")
print(f"{ders_2_ortalama[0]} Ortalama: {ders_2_ortalama[1]:.2f}")
print(f"{ders_3_ortalama[0]} Ortalama: {ders_3_ortalama[1]:.2f}")
