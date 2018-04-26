def engagement_rate(bs,ys,ps,ics,ts):
    grup=input("Grubunuzu giriniz(YBS1/YBS2/YBS3):")
    etkilesim_orani=(((bs+ys+ps)/ics)/ts)*100
    if (etkilesim_orani>0.2):
        print("{} grubunun etkileşim oranı {} hesaplanmıştır. Başarılı!".format(grup,etkilesim_orani))
        return etkilesim_orani
    else:
        print("{} grubunun etkileşim oranı {} hesaplanmıştır. Başarısız!".format(grup,etkilesim_orani))
        return etkilesim_orani

