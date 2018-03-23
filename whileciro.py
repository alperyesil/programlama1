print("""*****************
Ciro Hesaplama
*****************
""")

sm=500
bsf=20
ciro=5000
i=0
while True:
    sm=sm+200
    bsf=bsf+10
    ciro=sm*bsf
    i=i+1
    if (ciro>500000):
        print("{} Yıl Sonra Ciro 500.000 TL'den Fazla Olur.".format(i/12))
        break

