toplam=0

while True:
    girilen=float(input("Bir sayı giriniz (Çıkmak için '0':"))
    if (girilen==0):
        print("Programdan çıktınız.")
    else:
        kalan=girilen%3
        toplam=toplam+kalan
        print("Girdiğiniz Sayıların 3 İle Bölümünden Kalanların Toplamı:", toplam)

