
#! GÜVENLİ ŞİFRE OLUŞTURUCU !#
import random

print("Güvenli Şifre Oluşturucu\n")
karakterler_küçük = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "t", "u", "ü", "v", "y", "z"]
karakterler_büyük = ["A,", "B", "C", "D", "E", "F", "G", "H", "İ", "J", "K", "L", "M", "N", "O","Ö", "P", "R", "S", "T", "U", "Ü", "V", "Y", "Z"]
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
özel_karakterler = ["!", "+", "%", "/", "(", ")", "=", "?", "_", ">", "£", "#", "$", "$", "{", "[", "]", "}", "|", "*", "-", "@", "€", ".", ":", ",", ";"]
tümü = karakterler_büyük + karakterler_küçük + sayilar + özel_karakterler

karakter_sayisi = int(input("Karakter sayısını giriniz: "))
uygulama = input("Şifrenin hangi uygulamaya ait olduğunu yazınız (opsiyonel): ")
if uygulama == "":
    uygulama = "None"
else:
    pass

sifre = str("")
loop = 0
while loop != karakter_sayisi:
    sifre += str(random.choice(tümü))
    loop = loop+1
print("Oluşturulan şifreniz:", sifre)
with open ("C:\\projeler\\sifre_olusturucu.log", "a", encoding="utf-8") as dosya:
    dosya.write(uygulama + " : " + sifre + "\n")
print("\nUyarı! Şifreniz 'C:\projeler\sifre_olusturucu.log' konumuna kaydedildi!\n")
input("Çıkmak için enter tuşuna basınız...")