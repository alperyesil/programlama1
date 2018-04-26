iska=0
gel=0
gid=0
tciro=0
tcsayisi=0
aciro=0
def isletme_kar_hesaplama(iska,gel,gid):
    """Bu fonksiyon, işletme kârını hesaplar."""
    gel=float(input("Geliri giriniz:"))
    gid=float(input("Gideri giriniz:"))
    iska=gel-gid
    print("İşletme Kârı {}TL'dir.".format(iska))
    return iska

def adambasi_ciro(tciro,tcsayisi,aciro):
    """Bu fonksiyon, adambaşı ciro değerini hesaplar."""
    tciro=float(input("Toplam ciro değerini giriniz:"))
    tcsayisi=float(input("Toplam çalışan sayısını giriniz:"))
    aciro=tciro/tcsayisi
    print("Adambaşı ciro değeri:",aciro)
    return aciro
