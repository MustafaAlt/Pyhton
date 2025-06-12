# MUSTAFA ALTIPARMAK 21100011032 ODEV3
while True:
    import random
    import os

    print(""" 
     ========MAYIN-TARLASI-OYUNU======
    |    Yeni oyun için herhangi      |
    |         bir tuşa basın.         |
    |    Çıkış için 0'ı tuşlayınız    |
     ================================= 
    """)
    oyundevam = input("\t\t\t\t\t\t\t\t\t  SEÇİMİNİZ:")
    if oyundevam == "0":
        break
    else:
        os.system('cls')
        print("1-)GİZLİ MOD (Standart mayın tarlası oyunu modu.)\n"
              "2-)AÇIK MOD (Mayınların yeri oyunda görünür.)")
        oyundevam = input("\t\t\t\t SEÇİMİNİZ:")
        matris_boyutu = int(input("OYUNUN OYNANACAĞI KARE ZEMİNİN BOYUTUNU GİRİNİZ:"))
        if matris_boyutu < 10:
            print("Oyun alanı en az 10br olmalıdır.")
            continue
        zemin_ = []
        zemin_ = [["?"] * matris_boyutu for i in range(matris_boyutu)]
        mayinlar = []
        while len(mayinlar) < matris_boyutu * matris_boyutu * 3 // 10: # Mayin sayısı istediğimiz kadar oluncaya kadar dön.
            x = random.randint(0, matris_boyutu - 1) #  matris içinde eandom iki x ve y değeri ürettirdim.
            y = random.randint(0, matris_boyutu - 1)
            if [x, y] not in mayinlar: #bu üretilen nokta daha önce üretilmediyse bunu mayinlar listesine ekledim.
                mayinlar += [[x, y]]
        if oyundevam == "2": # eğer oyun açık modda oynanacak ise mayınların olduğu yerlere "?"  karakteri bastırdım.
            for i in range(matris_boyutu):
                for z in range(matris_boyutu):
                    if [i, z] in mayinlar:
                        zemin_[i][z] = "\033[1;31;40m?\033[0m" #renk kodlarını internetten yardım aldım hocam karakteri kırmızı olarak bastım
        for i in range(matris_boyutu):
            for z in range(matris_boyutu):
                print(zemin_[i][z], sep="\t\t\t", end=" ")
            print("\n")

        hamle = 0
        noktalar = []
        while True:

            noktax = int(input("Açmak istediğiniz noktanın satır kordinatını giriniz:")) - 1
            noktay = int(input("Açmak istediğiniz noktanın sütun kordinatını giriniz:")) - 1
            if 0 > noktay or noktay >= matris_boyutu or 0 > noktax or noktax >= matris_boyutu:
                print("Lütfen geçerli aralıklarda kordinat giriniz.")
                continue
            nokta = [noktax, noktay]
            if nokta not in noktalar:
                noktalar += [[noktax, noktay]]
            else:
                print("Bu kordinatı daha önce açtınız.Lütfen tekrar deneyiniz.")
                continue
            if nokta in mayinlar:  # 65.satırdaki else nokta mayınlarda değilse drumu için geçerli. (ters yapmak daha iyi olurdu olasılık olarak hocam bunu yeni fark ettim:)
                print("\n\n\n \033[1;31;40mÜZGÜNÜM MAYINA BASTIN\033[0m\n \033[1;31;40m Puanınız:{} \033[0m\n".format(
                    hamle))
                for i in range(matris_boyutu): # basılan mayından sonra tüm mayınların olduğu yer x ile değiştirip aşşağıdaki fonskşyonda yazdırdım.
                    for z in range(matris_boyutu):
                        if [i, z] in mayinlar:
                            zemin_[i][z] = "\033[1;31;40mX\033[0m"
                for i in range(matris_boyutu):
                    for z in range(matris_boyutu):
                        print(zemin_[i][z], sep="\t\t\t", end=" ")
                    print("\n")
                break
            else: # bu nokta bir mayın değilse
                hamle += 1
                kontrol = 0 #  bu kontrol değişkeni noktanın etrafındaki noktaları gezdikten sonra her mayında artıyor.ve açılmak istenen yerin yerine yazılıyor.
                for i in range(noktax - 1, noktax + 2): # i noktanın etrafındaki noktaların satırlarını geziyor. z de sutun değeğrlerini geziyor.
                    for z in range(noktay - 1, noktay + 2): # 1 artırıp azaltmak yeterli oldu çünkü noktanın etrafında maks satır ve sutun değeri 1 artıp azalıyor. yani (1,1) noktası için
                        if [i, z] in mayinlar and [i, z] != nokta:         #kontrol edilmesi gereken noktalar: (0,0) (0,1) (0,2)  (1,0) (1,1) (1,2)   (2,0) (2,1) (2,2)
                            kontrol += 1 # burda da artıyor.               # [i, z] != nokta  ifadesi ile nokta kendisi değilse diyorum yani kendini kontrol etmiyor.
                zemin_[noktax][noktay] = "\033[32;40m{}\033[0m".format(kontrol) # kontrol ile kaç adet mayın varsa o değeri değiştiriyorum
                for i in range(matris_boyutu):
                    for z in range(matris_boyutu):
                        print(zemin_[i][z], sep="\t\t\t", end=" ")
                    print("\n")
                if hamle == ((matris_boyutu * matris_boyutu) - (matris_boyutu * matris_boyutu * 3 // 10)):   # yapılan hamle sayısı matristeki mayınsız alan kadar olduğunda oyun bitiyor.
                    print("\033[32;40mTEBRİKLER OYUNU KAZANDINIZ\033[0m\n\033[32;40mPUANINIZ:{}\033[0m ".format(hamle))
                    break

