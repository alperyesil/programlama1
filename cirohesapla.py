print("""*****************
Ciro Hesapla(Beta)
*****************
""")


sm=float(input("Satış miktarını giriniz:"))
bsf=float(input("Birim satış fiyatını giriniz:"))
tcs=25

def fciro(sm,bsf):
    ciro=sm*bsf
    print("Ciro değeri {}TL olarak hesaplanmıştır.".format(ciro))
def faciro(sm,bsf,tcs):
    aciro=(sm*bsf)/tcs
    print("Adambaşı ciro değeri {}TL olarak hesaplanmıştır".format(aciro))

fciro(sm,bsf)
faciro(sm,bsf,tcs)
