print("""*****************
Stok Hesaplama(Beta)
*****************
""")

ksay=200
ysay=150
dsay=100
satksay=25
satysay=20
satdsay=10
alksay=10
alysay=15
aldsay=5


def fdbstok(ksay,ysay,dsay):
    print("Dönembaşı Stok:{} adet koltuk,{} adet yatak, {} adet dolap".format(ksay,ysay,dsay))

def fdsstok(ksay,ysay,dsay,satksay,satysay,satdsay,alksay,alysay,aldsay):
    global dsksay
    dsksay=ksay+alksay-satksay
    global dsysay
    dsysay=(ysay+alysay-satysay)
    global dsdsay
    dsdsay=(dsay+aldsay-satdsay)
    print("Dönemsonu Stok:{} adet koltuk, {} adet yatak, {} adet dolap".format(dsksay,dsysay,dsdsay))

def fortstok(ksay,ysay,dsay,dsksay,dsysay,dsdsay):
    ortksay=(ksay+dsksay)/2
    ortysay=(ysay+dsysay)/2
    ortdsay=(dsay+dsdsay)/2
    print("1 Yıllık Ortalama Stok: {} adet koltuk, {} adet yatak, {} adet dolap".format(ortksay,ortysay,ortdsay))

fdbstok(ksay,ysay,dsay)
fdsstok(ksay,ysay,dsay,satksay,satysay,satdsay,alksay,alysay,aldsay)
fortstok(ksay,ysay,dsay,dsksay,dsysay,dsdsay)










