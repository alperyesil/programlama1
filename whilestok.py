print("""*****************
Stok Hesaplama
*****************
""")

sm=10000
au=100
su=500
fark=au-su
i=0
while(sm>0):
    sm=sm+fark
    i=i+1
print("{} ayda stok tükenecektir.".format(i))