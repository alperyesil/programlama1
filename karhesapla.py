print("""****************
Kâr Hesapla(Beta)
****************
""")

finansmanGelir=float(input("Finansman gelirini giriniz:"))
pazarGelir=float(input("Pazar gelirini giriniz:"))
kiraGelir=float(input("Kira gelirini giriniz:"))
ucret=float(input("Ücreti giriniz:"))
finansmanGider=float(input("Finansman giderini giriniz:"))
pazarGider=float(input("Pazar giderini giriniz:"))
kiraGider=float(input("Kira giderini giriniz:"))
muhasebeGider=float(input("Muhasebe giderini giriniz:"))

gelir=finansmanGelir+pazarGelir+kiraGelir
gider=ucret+finansmanGider+pazarGider+kiraGider+muhasebeGider
kar=gelir-gider

if (kar>=1000):
    print ("Şirketiniz {} TL kâr etmiştir ve kârlıdır.".format(kar))
else:
    print("Şirketiniz kârlı değildir, kârlı sayılabilmesi için {} TL daha kâr etmesi gerekmektedir.".format(1000-kar))




