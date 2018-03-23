print("""*****************
Defolu Ürün Hesaplama
*****************
""")
gdus=0
tdus=0
gus=200
g=0
while True:
    gdus=int(input("Defolu Ürün Adedi:"))
    tdus=tdus+gdus
    g+=1
    if (gdus<=gus/5):
        print("{} Günlük Toplam Defolu Ürün Sayısı {} Hesaplanmıştır".format(g,tdus))
    else:
        print("Günlük Defolu Ürün Limiti Aşıldı!")
        break