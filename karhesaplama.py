print("""*****************
Kâr Hesaplama(Beta)
*****************
""")

yage1=float(input("ilk 6 ay içindeki yazılım gelirini giriniz:"))
fige1=float(input("ilk 6 ay içindeki finansman gelirini giriniz:"))
usg1=float(input("İlk 6 ay içindeki ürün satış gelirini giriniz:"))
yage2 = float(input("Son 6 ay içindeki yazılım gelirini giriniz:"))
spge2 = float(input("Sponsorluk gelirini giriniz:"))
usg2 = float(input("Son 6 ay içindeki ürün satış gelirini giriniz:"))
etge2 = float(input("E-ticaret gelirini giriniz:"))
cama1 = float(input("İlk 6 ay içindeki çalışan maaş giderini giriniz:"))
kigi1 = float(input("İlk 6 ay içindeki kira giderini giriniz:"))
doma1 = float(input("Donanım maliyetini giriniz:"))
cama2 = float(input("Son 6 ay içindeki çalışan maaş giderini giriniz:"))
kigi2 = float(input("Son 6 ay içindeki kira giderini giriniz:"))
bama = float(input("Bakım maliyetini giriniz:"))
def filk6aygelir(a,b,c):
    d=(a+b+c)
    print("İlk 6 aylık toplam gelir:",d)
    return(d)
def fson6aygelir(a,b,c,d):
    e=(a+b+c+d)
    print("Son 6 aylık toplam gelir:",e)
    return(e)
def filk6aygider(a,b,c):
    d=(a+b+c)
    print("İlk 6 aylık toplam gider",d)
    return(d)
def fson6aygider(a,b,c):
    d=(a+b+c)
    print("Son 6 aylık toplam gider:",d)
    return(d)

ilk6aykar=filk6aygelir(yage1,fige1,usg1)-filk6aygider(cama1,kigi1,doma1)
son6aykar=fson6aygelir(yage2,spge2,usg2,etge2)-fson6aygider(cama2,kigi2,bama)

if (ilk6aykar-son6aykar>5000):  #Soruda "ilk 6 aylık ve son 6 aylık İşletme kârı arasındaki farkı bularak" kârlılık değerlendirmemiz istendiği için
    print("İşletme çok kârlı.")
elif (1000<=ilk6aykar-son6aykar<=5000):
    print("İşletme kârı normal.")
else:
    print("İşletme yeterince kârda değil.")



