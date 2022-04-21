sayi=int(input("sayi giriniz "))
KAREKOK=sayi ** 0.5
if KAREKOK==int(KAREKOK):
    print(KAREKOK="tam sayıdır")
else:
    print("tam kare değildir ")

metin=(input("kelime gir"))
sozluk=dict()
for harf in metin:
    if harf in sozluk:
        sozluk[harf] +=1
    else:
        sozluk[harf] =1

for harf,adet in sozluk.items():
    print(harf,adet)