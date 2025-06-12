# 21100011032 Mustafa Altıparmak Final Projesi
def anamenu():
    print("""\n 1->Ürün Ekle
 2->Ürün Sil
 3->Stok Sorgula (ürün koduna göre)
 4->Stok Sorgula (Marka Adına Göre)
 5->SuperMarket Toplam Stoğu Sorgula
 6->Son Kullanma Tarihi geçen ürünleri sorgula
 7->Satış Yap
 8->Ürün bilgisi güncelle
 9->Kar hesapla 
 10->Kasayı Kapat\n""")

    while True:
        try:
            islem1 = int(input("Lütfen yapmak istediğiniz işlemi seçiniz: "))
            if islem1 < 1 or islem1 > 10:
                print("Geçersiz bir işlem numarası girdiniz. Lütfen 1 ile 10 arasında bir sayı girin.")
            else:
                break
        except ValueError:
            print("Geçersiz bir giriş yaptınız. Lütfen sayısal bir değer girin.")

    return islem1


def gecis_islemleri(islem2):
    if islem2 == 1:
        urunEkle()
    elif islem2 == 2:
        urunsil()
    elif islem2 == 3:
        stoksorgula3()
    elif islem2 == 4:
        stoksorgulaada()
    elif islem2 == 5:
        toplamstok()
    elif islem2 == 6:
        sontarihkontrol()
    elif islem2 == 7:
        satisyap()
    elif islem2 == 8:
        guncelle()
    elif islem2 == 9:
        karhesapla()
    elif islem2 == 10:
        listedencikar()
        verileriyaz()
        with open("urunlistesidosya.txt", "r") as urunlistesidosya:
            urunlistesidosya.seek(0)
        satilanuurunleriyaz()


def gecis_islemleri_sor():
    while True:
        try:
            islem3 = input("""\n
            \t0->Kasayı kapat.
            \t1-> Ana menüye dön.
            \n""")
            if int(islem3) < 0 or int(islem3) > 1:
                print("Hatalı tuslama yaptınız.")
            else:
                break
        except ValueError:
            print("Hatalı tuslama yaptınız.")

    if islem3 == "1":
        islem = anamenu()
        gecis_islemleri(islem)
    else:
        listedencikar()
        verileriyaz()
        with open("urunlistesidosya.txt", "r") as urunlistesidosya:
            urunlistesidosya.seek(0)
        satilanuurunleriyaz()


def urunEkle():
    global urunlistesi
    sayi = 0
    alis = 0
    satis = 0
    sonkllnm = 0
    adeti = 0
    while True:
        try:
            sayi = int(input("Kaç farklı ürün eklemek istiyorsunuz: "))
            if sayi < 1:
                print("Geçersiz bir değer girdiniz. Lütfen pozitif bir sayı girin.")
            else:
                break
        except ValueError:
            print("Geçersiz bir giriş yaptınız. Lütfen sayısal bir değer girin.")

    baslangic = len(urunlistesi)

    for i in range(baslangic + 1, sayi + baslangic + 1):
        while True:
            try:
                kodu = input("{}. ürünün ürün kodunu giriniz: ".format(i))
                int(kodu)
                if int(kodu) < 100:
                    print("Ürün kodları 100'den büyük olmalı.")
                else:
                    break
            except ValueError:
                print("lütfen ürün kodunu sadece rakamlarla giriniz.")

        marka = input("{}. ürünün markasını giriniz: ".format(i))
        marka = marka.upper()
        while True:
            kontrol = 0
            try:
                alis = input("{}. ürünün alış fiyatını giriniz: ".format(i))
                int(alis)
            except ValueError:
                kontrol = 1
                print("lütfen sadece rakam giriniz.")
            if kontrol == 0:
                break
        while True:
            kontrol = 0
            try:
                satis = input("{}. ürünün satış fiyatını giriniz: ".format(i))
                int(satis)
            except ValueError:
                kontrol = 1
                print("lütfen sadece rakam giriniz.")
            if kontrol == 0:
                break
        while True:
            kontrol = 0
            try:
                sonkllnm = input("{}. ürünün son kullanma yılını giriniz: ".format(i))
                int(sonkllnm)
            except ValueError:
                kontrol = 1
                print("lütfen sadece rakam giriniz.")
            if kontrol == 0:
                break
        while True:
            kontrol = 0
            try:
                adeti = input("{}. ürünün adetini giriniz: ".format(i))
                int(adeti)
            except ValueError:
                kontrol = 1
                print("lütfen sadece rakam giriniz.")
            if kontrol == 0:
                break
        urun = [kodu, marka, alis, satis, sonkllnm, adeti]
        urunlistesi.append(urun)

    gecis_islemleri_sor()


def urunsil():
    silinecek = int(input("Silmek istediğiniz ürünün kodunu giriniz: "))
    uzunluk = len(urunlistesi)

    for i in range(uzunluk):
        if int(urunlistesi[i][0]) == silinecek or urunlistesi[i][5] == 0:
            del urunlistesi[i]
            break

    gecis_islemleri_sor()


def stoksorgula3():
    kontrol = 0
    sorgu = input("sorgulamak istediğiniz urunun urun kodunu giriniz:")
    for i in range(len(urunlistesi)):
        if urunlistesi[i][0] == sorgu:
            kontrol = 1
            print("""aradığınız ürün bilgileri:
                  ürün kodu:{}
                  ürün markası:{}
                  ürün alış fiyatı:{}
                  ürün satış fiyatı:{}
                  ürün son kullanma tarihi:{}
                  ürün adeti : {}""".format(urunlistesi[i][0], urunlistesi[i][1], urunlistesi[i][2], urunlistesi[i][3],
                                            urunlistesi[i][4], urunlistesi[i][5]))
    if kontrol == 0:
        print("Maalesef stoklarda bu urun bitmiş.Yakında temin edeceğiz.")
    gecis_islemleri_sor()


def stoksorgulaada():
    sorgu = input("sorgulamak istediğiniz markayı giriniz:")
    sorgu = sorgu.upper()
    kontrol = 0
    for i in range(len(urunlistesi)):
        if str(urunlistesi[i][1]) == sorgu:
            kontrol = 1
            print("""aradığınız ürün bilgileri:
                      ürün kodu:{}
                      ürün markası:{}
                      ürün alış fiyatı:{}
                      ürün satış fiyatı:{}
                      ürün son kullanma tarihi:{}
                      ürün adeti : {}""".format(urunlistesi[i][0], urunlistesi[i][1], urunlistesi[i][2],
                                                urunlistesi[i][3],
                                                urunlistesi[i][4], urunlistesi[i][5]))
    if kontrol == 0:
        print("Maalesef stoklarda bu urun bitmiş.Yakında temin edeceğiz.")
    gecis_islemleri_sor()


def toplamstok():
    topstok = []
    for i in range(len(urunlistesi)):

        if int(urunlistesi[i][5]) > 0:
            topstok += [[urunlistesi[i][0]] + [urunlistesi[i][5]]]

    for i in range(len(topstok)):
        print("""
        ({}) kodlu ürünün adet sayısı :{}
        """.format(topstok[i][0], topstok[i][1]))
    gecis_islemleri_sor()


def verilerioku():
    global urunlistesi
    with open("urunlistesidosya.txt", "r") as urunlistesidosya:
        urunlistesi = urunlistesidosya.readlines()
        urunlistesidosya.seek(0)


def listeyecevir():
    global urunlistesi
    liste3 = []
    for i in urunlistesi:
        liste2 = i.split("-")
        if len(liste2) == 6:
            liste3.append(liste2)
    urunlistesi = liste3


def listedencikar():
    global urunlistesi
    liste1 = ""
    for i in urunlistesi:
        for j in i:
            liste1 += j + "-"

        liste1 = liste1[:-1]
        liste1 += "\n"

    urunlistesi = liste1


def verileriyaz():
    global urunlistesi

    with open("urunlistesidosya.txt", "w") as urunlistesidosya:
        urunlistesidosya.write(urunlistesi)
        urunlistesidosya.seek(0)


def sontarihkontrol():
    global urunlistesi
    mevcutyil = int(input("mevcut yılı giriniz:"))
    kontrol = 0
    for i in range(len(urunlistesi)):

        if int(urunlistesi[i][4]) < mevcutyil:
            kontrol = 1
            print("{} kodlu urunun son kullanma tarihi geçmiş.".format(urunlistesi[i][0]))
    if kontrol == 0:
        print("Tarihi geçmiş ürün bulunmamaktadır...")
        gecis_islemleri_sor()
    else:
        cevap = int(input("Bu urunleri silmek icin 0'ı tuslayınız.Devam etmek için herhangi bir tusa basınız."))
        if cevap != 0:
            gecis_islemleri_sor()
        else:
            geciciliste = []
            for i in range(len(urunlistesi)):
                if int(urunlistesi[i][4]) >= mevcutyil:
                    geciciliste.append(urunlistesi[i])
            urunlistesi = geciciliste

            gecis_islemleri_sor()


def satisyap():
    global satilanurunler
    satisyapilanurun = input("satisi yapilan ürünün kodunu giriniz:")
    kontrol = 0
    for i in range(len(urunlistesi)):
        if urunlistesi[i][0] == satisyapilanurun:
            kontrol = 1
    if kontrol == 0:
        print("Bu urun stoklarımzda bulunmamaktadır.")
        gecis_islemleri_sor()
    satisadeti = int(input("kac adet satis yapıldı:"))
    liste1 = ((satisyapilanurun, satisadeti),)
    satilanurunler += liste1
    for i in range(len(urunlistesi)):

        if urunlistesi[i][0] == satisyapilanurun:

            if int(urunlistesi[i][5]) < satisadeti:
                print("istenilen kadar stok bulunmamaktadır.")

                gecis_islemleri_sor()
            else:
                urunlistesi[i][5] = str(int(urunlistesi[i][5]) - satisadeti)
                print(urunlistesi[i][5])

    gecis_islemleri_sor()


def satilanurunlerioku():
    global satilanurunler
    with open("satilanurunler.txt", "r") as satilanurunlerdosya:
        satilanurunler = satilanurunlerdosya.readlines()
    demet = []
    for i in satilanurunler:
        ayrilmis = tuple(
            i.strip().split('-'))  # hocam burda internetten yardım aldım. mantığını anladım ama kendim kuramadım.
        demet.append(ayrilmis)

    satilanurunler = tuple(demet)


def satilanuurunleriyaz():
    global satilanurunler
    liste1 = ""
    for i in range(len(satilanurunler)):
        for j in range(len(satilanurunler[0])):
            if j == 0:
                liste1 += str(satilanurunler[i][j]) + "-"
            elif j == 1:
                liste1 += str(satilanurunler[i][j]) + "\n"
    with open("satilanurunler.txt", "w") as satilanurunlerdosya:
        satilanurunlerdosya.writelines(liste1)


def guncelle():
    global urunlistesi
    istenen = input("güncellemek istediğiniz ürünün kodunu giriniz:")
    verisi = int(input("""
    1->ürün kodu
    2->ürün marka adı 
    3->ürün alış fiyatı
    4->ürün satis fiyatı
    5->ürün son kullanma tarihi
    6->ürün adeti
    bu ururnun hangi bilgisini güncellemek istiyorsunuz:"""))
    degistir = input("yeni veriyi giriniz:")
    degistir = degistir.upper()
    for i in range(len(urunlistesi)):
        for j in range(len(urunlistesi[0])):
            if urunlistesi[i][0] == istenen:
                urunlistesi[i][verisi - 1] = degistir
    gecis_islemleri_sor()


def karhesapla():
    global satilanurunler
    toplam = 0
    yasa = int(input("\n\tToplam karı hesaplamak için 1'i belirli bir ürünün karını öğrenmek için 0'ı tuşlayınız:"))
    if yasa == 1:
        for i in range(len(satilanurunler)):
            for z in range(len(urunlistesi)):
                if urunlistesi[z][0] == satilanurunler[i][0]:
                    toplam += (int(urunlistesi[z][3]) - int(urunlistesi[z][2])) * int(satilanurunler[i][1])
        print("\n\tSuana kadar yapılan satislarda elde edilen toplam kar:{}\n".format(toplam))
        gecis_islemleri_sor()
    elif yasa == 0:
        kimseyitanimadimben = input("ürünün barkod numarasını giriniz:")
        for i in range(len(satilanurunler)):
            for z in range(len(urunlistesi)):
                if urunlistesi[z][0] == satilanurunler[i][0] == kimseyitanimadimben:
                    toplam += (int(urunlistesi[z][3]) - int(urunlistesi[z][2])) * int(satilanurunler[i][1])
        print("\n\tBu urunden toplam {} tl kar elde edildi.\n".format(toplam))
        gecis_islemleri_sor()


satilanurunler = ()
urunlistesi = []
satilanurunlerioku()
verilerioku()
listeyecevir()
islem = anamenu()
gecis_islemleri(islem)
