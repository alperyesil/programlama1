#Katma Değer Ciro = Toplam Satış Miktarı – (Hammadde maliyeti + Bakım Onarım Giderleri +
#Sevkiyat Giderleri + Satın Alınan Hizmet Giderleri)

tsm=float(input("Toplam Satış Miktarını Giriniz:"))
hm=float(input("Hammadde Maliyetini Giriniz:"))
bog=float(input("Bakım Onarım Giderlerini Giriniz:"))
sg=float(input("Sevkiyat Giderlerini Giriniz:"))
sahg=float(input("Satın Alınan Hizmet Giderlerini Giriniz:"))

def fkdciro(tsm,hm,bog,sg,sahg):
    kdciro=tsm-(hm+bog+sg+sahg)
    if (kdciro>1000):
        print("İşletme Katma Değer Cirosu Yüksek")
    elif (499<kdciro<1000):
        print("İşletme Katma Değer Cirosu Normal")
    else:
        print("İşletme Katma Değer Cirosu Düşük")
fkdciro(tsm,hm,bog,sg,sahg)