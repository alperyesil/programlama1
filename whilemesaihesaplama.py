print("""*****************
Maaş Gideri Hesaplama
*****************
""")

maxmes=22
hmesai1=""
c=50
m=1800 #4x5x90
ekyev=9 #9*0.10
while True:
    hmesai1= int(input("1.Haftadaki Mesai Saatini Giriniz:"))
    hmesai2= int(input("2.Haftadaki Mesai Saatini Giriniz:"))
    hmesai3= int(input("3.Haftadaki Mesai Saatini Giriniz:"))
    hmesai4= int(input("4.Haftadaki Mesai Saatini Giriniz:"))

    if (hmesai1+hmesai2+hmesai3+hmesai4> maxmes):
        print("Aylık Mesai {} Değerinden Fazla Olamaz!".format(maxmes))
    else:
        topmaas=c*((m)+(hmesai1*ekyev))
        print("Personele Ödenen Toplam Maaş(Aylık):", topmaas)
        print("Personele Ödenen Toplam Maaş(Yıllık):",topmaas*12)
        break
