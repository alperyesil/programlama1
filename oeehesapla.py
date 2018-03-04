print("""*****************
OEE Hesapla(Beta)
*****************
""")

pus=float(input('Planlanan üretim süresini giriniz:'))
pd=float(input('Plansız duruşu giriniz:'))
if (pus==pd):
    print("Planlanan üretim süresi, plansız duruşla aynı olursa OEE hesaplanamaz.")
else:

    scz=float(input('Standart çevrim zamanını giriniz:'))
    um=float(input('Üretim miktarını giriniz:'))
    sum=float(input('Sağlam ürün miktarını giriniz:'))
    tum=float(input('Toplam üretim miktarını giriniz:'))

    def fkullan(pus,pd):
        kullan=(pus-pd)/pus
        print("Kullanılabilirlik oranı:",kullan)
        return kullan

    def fperf(scz,um,pus,pd):
        perf=(scz*um)/(pus-pd)
        print("Performans oranı:",perf)
        return perf

    def fkal(sum,tum):
        kal=sum/tum
        print("Kalite Oranı:",kal)
        return kal

    oee=fkullan(pus,pd)*fperf(scz,um,pus,pd)*fkal(sum,tum)*100
    print("Ekipman Etkinlilik Oranı(OEE):",oee)



