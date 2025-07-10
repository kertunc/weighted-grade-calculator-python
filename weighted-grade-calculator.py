#Kullanıcıdan vize, proje ve final notlarını alıp, ağırlıklı ortalamayı hesapla.
#Ardından hem ortalamayı hem de geçip geçmediğini ekrana yazdır.

vize = input("Vize notunu giriniz: ")
proje = input("Proje notunu giriniz: ")
final = input("Final notunu giriniz: ")

vize = float(vize) * 0.30
proje = float(proje) * 0.20
final = float(final) * 0.50

ortalama = vize + proje + final

print("Ogrencinin not ortalamasi = " + str(round(ortalama, 2)))

if ortalama >= 50:
    print("Ogrenci dersten gecmistir!")
else:
    print("Ogrenci dersten gecememistir!")

if ortalama >= 85:
    print("Harf notu = AA")
elif ortalama >= 70:
    print("Harf notu = BB")
elif ortalama >= 50:
    print("Harf notu = CC")
elif ortalama >= 30:
    print("Harf notu = DD")
elif ortalama >= 0:
    print("Harf notu = FF")
