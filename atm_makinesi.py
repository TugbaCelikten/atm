print("""**************************
Atm Makinesine Hoşgeldiniz
İşlemler:
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q' ya basınız.
**************************""")
bakiye = 1000

while True:
    islem= input("İşlem Seçiniz")

    if(islem=="q"):
        print("Yine bekleriz")
        break
    elif(islem=="1"):
        print("Bakiyeniz: {} TL'dir.".format(bakiye))
    elif(islem=="2"):
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz"))
        bakiye+=miktar
        print("Bakiyeniz: {} TL'dir.".format(bakiye))
    elif(islem=="3"):
        miktar = int(input("Çekmek istediğiniz miktarı giriniz"))
        if(bakiye-miktar<0):
            print("Yetersiz bakiye!")
            continue

        bakiye-=miktar
        print("Bakiyeniz: {} TL'dir.".format(bakiye))
    else:
        print("Geçersiz işlem...")