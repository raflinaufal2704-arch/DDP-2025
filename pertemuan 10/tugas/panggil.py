import bangundatar as bd, bangunruang as br

print("============bangun datar==============")
print(f"hasil dari luas persegi {bd.persegi(5)}")
print(f"hasil dari luas persegi panjang{bd.persegipanjang(6,3)}")
print(f"hasil dari luas segitiga{bd.segitiga(7,9)}")
print(f"hasil dari luas lingkaran{bd.lingkaran(8)}")
print(f"hasil dari luas jajar genjang{bd.jajargenjang(12,3)}")

print("============bangun ruang===============")
print(f"volume dari kubus{br.kubus(5)}")
print(f"volume dari balok{br.balok(3, 2, 4)}")
print(f"volume dari prisma{br.prisma(8, 3)}")
print(f"volume dari tabung{br.tabung(9, 5)}")
print(f"volume dari kerucut{br.kerucut(12,13)}")
