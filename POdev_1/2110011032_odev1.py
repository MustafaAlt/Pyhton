# MUSTAFA ALTIPARMAK 21100011032
a = 1        #Hocam sonsuz döngüler sürekli lazım olduğu için global olarak bi a değişkeni tanımladım.
while a == 1:   # Tüm işlemleri bu sonsuz döngü içerisinde yaptım. Bu sayede kişi çıkış yapmadığı sürece tekrar edecek.
    print("""
    \t 1-) 10'luk tabandan 2'lik tabana cevirme 
    \t 2-)  2'lik tabandan 10'luk tabana cevirme 
    \t 3-) cıkıs
    """)
    secim = int(input("lutfen yapmak istediginiz islemi seciniz:"))
    if secim == 1:

        sayi1 = int(input("Lütfen 2'lik tabana cevirmek istediginiz sayiyi giriniz:"))
        sayi = sayi1                                            # Sayıyı kaybetmemek için farklı bir değişkene atadım.
        if sayi < 0:                                             # sayının negatif olması drumu ve pozitif olması drumu için farklı işlemler kullandım.
           sayi = sayi * (-1)                                     #Sayıyı önce pozitife çevirdim.
           cevrilmis = "1"                                        # Burda içinde 1 olan string ifade tanımladım. dönüşümdeki ilk rakam 1 olması için.
           while a == 1:                                          # Tekrar sonsuz döngü oluşturudm. bitme şartı sayının artık bölünememesi drumunda.
               ara = (sayi % 2)
               if ara == 0:                                       # Eğer sayının modu "1" çıkarsa "0" eğer "0" çıkarsa "1" yazdım.
                   cevrilmis = cevrilmis+"1"
               else :
                   cevrilmis = cevrilmis+"0"
               sayi = sayi // 2
               if sayi < 2:                                       # Her döngüde sayıyı kontrol ettim.Sayı 2 den küçükse dögü bitirdim.
                   if sayi == 0:
                       cevrilmis = cevrilmis + "1"                # sayının son bölümden elde ettiğimiz sonucunu da ekledim.
                   else:
                       cevrilmis = cevrilmis + "0"
                   sayi = sayi // 2
                   break
        elif sayi > 0:                                             # Sayının pozitif olması drumu için.
         cevrilmis = ""                                            # Burda içi boş olan string ifade tanımladım.
         while a == 1:
            cevrilmis = cevrilmis + str(sayi % 2)                  # Burada moddan ulaştığımız sayıyı direk str ile cast ettim ve topladm
            sayi = sayi // 2
            if sayi < 2:
                cevrilmis = cevrilmis + str(sayi)
                break
         print("\n\t({})₁₀ = ({})₂\n".format(sayi1 , cevrilmis[::-1]))
        continue
    elif secim == 2:
        sayi3 = input("Lütfen 10'luk tabana cevirmek istediginiz sayiyi giriniz:")
        uzunluk = len(sayi3)
        toplam = 0
        kontrol = 0
        for i in range(0, uzunluk):                                    # sayının elemlarının binary sisteme uyup uymadıklarını kontrol ettim.
            if int(sayi3[i]) >= 2 or int(sayi3[i]) <= -1:
                print("Girdiğiniz sayı 2'lik sayı sistemine uymamaktadır.")
                kontrol = 1

        if kontrol == 1:
            continue # hocam döngü başına geçmesi için böyle bir çözüm buldum.
        for i in range(0, uzunluk):
            toplam += (int(sayi3[uzunluk - i - 1])) * (2 ** i)        # Sayının işlem yapılan elemanını cast ettim. 2 üzeri sırayla (0,1,2..) çaptım
        print("\n\t({})₂ = ({})₁₀\n ".format(sayi3, toplam))                # ve bunları da toplam değişkeinnide topladım.
        continue
    elif secim == 3:
       print("İyi günler.")
       break
    else:
     print("Yanlis tuslama yaptiniz lütfen tekrar tuslama yapiniz.")