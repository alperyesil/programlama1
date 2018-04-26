aktif=0
pasif=0

def aktif_hesapla(kash,alcekh,banh,alsenh,ticmalh,binah,tash,demh):
    aktif=kash+alcekh+banh+alsenh+ticmalh+binah+tash+demh
    print("Aktif toplamı {} TL'dir.".format(aktif))
    return aktif

def pasif_hesapla(kbkh,sath,ubkh,bsh,serh):
    pasif=kbkh+sath+ubkh+bsh+serh
    print("Pasif toplamı {} TL'dir.".format(pasif))
    return pasif

def bilanco_hesapla(aktif,pasif):
    if (aktif==pasif):
        print("Kapanış bilançosu doğru hesaplanmıştır.")
    else:
        print("Kapanış bilançosu yanlış hesaplanmıştır.")

