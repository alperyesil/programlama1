print("""*****************
Müşterilerle Çalışma Süresi Hesaplama(Beta)
*****************
""")
cs2016 = 170
tms2016 = 50
cs2017 = 220
tms2017 = 70

def fmcs(a,b,q):
    c = a / b
    print("{} yılındaki müşterilerle çalışma süresi:{}".format(q,c))
    return(c)

mcs2016=fmcs(cs2016,tms2016,"2016")
mcs2017= fmcs(cs2017,tms2017,"2017")

if (mcs2017 > mcs2016):
    print("2017'deki müşterilerle çalışma süresi 2016'ya göre {} artmıştır".format(mcs2017 - mcs2016))
elif (mcs2016>mcs2017):
    print("2017'deki müşterilerle çalışma süresi 2016'ya göre {} azalmıştır".format(mcs2016-mcs2017))
