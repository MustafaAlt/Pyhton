# MUSTAFA ALTIPARMAK 21100011032
Kelime_listesi = [
                "system", "data", "algorithm", "such", "base", "node", "model", "case", "program", "information",
                "set", "code", "function", "process", "application", "software", "class", "point", "type", "network",
                "tree", "object", "element", "input", "operation", "level", "memory", "table", "order", "file",
                "variable", "language", "write",	"list", "structure", "compute", "sequence", "computer", "bit",
                "probability", "machine", "array", "page", "error", "step", "search", "most", "path", "graph", "web",
                "length", "several", "security", "proof", "access", "obtain", "matrix", "task", "image", "form",
                "return", "interface", "resource", "address", "implementation", "loop",	"first", "read", "location",
                "hardware", "behavior", "programming", "field", "key",	"parameter", "distribution", "definition",
                "instance", "interaction", "internet", "representation",	"edge",	"stack", "return", "procedure",
                "link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                "detection", "write",	"execute", "least", "key"]
while True:
    import random
    print(""" 
     ========KELİME-TAHMİN-OYUNU======
    |    Yeni oyun için herhangi      |
    |         bir tuşa basın.         |
    |    Çıkış için 0'ı tuşlayınız    |
     ================================= 
    """)
    oyundevam = input("\t\tSEÇİMİNİZ:")
    if oyundevam == "0":
        break
    else:
        kelime = random.choice(Kelime_listesi)
        kelime_uzunlugu = len(kelime)                                                                # ilk baştaki printler kelime bilgileri
        print("\t\tKelimeniz {} harften oluşmaktadır.".format(kelime_uzunlugu), )
        bilinmeyen_kelime = ""                                                                       # üzerinde işlem yapacağım boş bir string  oluşturdum.
        for i in range(kelime_uzunlugu):
            bilinmeyen_kelime += "-"                                                                 # Kelime uzunluğu kadar "-" işareti bastırdım bilgi için.
        print("\t\t{}".format(bilinmeyen_kelime))
        if kelime_uzunlugu % 2 == 0:                                                                 # Kelime uzunluğuna göre hak tanımladım.
            tahminHak = kelime_uzunlugu // 2
        else:
            tahminHak = (kelime_uzunlugu + 1) // 2
        print("\t\tTahmin hakkınız: {} ".format(tahminHak))
        sesli_harfler = "aeıioöuü"                                                                                     # Daha sonra kullanmak için sesli harfleri tanımladım.
        puan = 0                                                                                   # genel puanı tanımladım her seferinde sıfırlanması için burda 0'a eşitledim.
        tahminler = ""                                                                     # aynı harfleri tekrar tekrar tahmin ediilmemesi için boş bşr string daha tanımladım.
        while True:                                                                            # sonsuz dögü açtım oyunun yanlış veya doğru sonucunda zaten kod en başa dönüyor.
            yapilan_tahmin = input("Tahmininizi giriniz:")
            yapilan_tahmin = yapilan_tahmin.lower()
            if len(yapilan_tahmin) != 1:
                print("lütfen bir harf girerek tahminde bulunun.")
                continue
            if yapilan_tahmin in tahminler:                                                                   # Yapılan tahmin daha önceden yapıldıysa tekrar tahmin istiyorum.
                print("Bu tahminde daha önce bulundunuz lütfen tekrar tahminde bulunun.")
                continue
            tahminler += yapilan_tahmin                                                         # Eğer daha önce tahmin edilmediyse burda tekrar tahmin edilmemsi için tutuyorm
            kac_kere_var = 0                                                           # Doğru tahminlerin 1 den fazla olması drumunda puan değişeceği için değişken tanımladım
            if yapilan_tahmin in kelime:
                for i in range(0, kelime_uzunlugu):
                    if kelime[i] == yapilan_tahmin:
                        kac_kere_var += 1
                        bilinmeyen_kelime = bilinmeyen_kelime[: i] + yapilan_tahmin + bilinmeyen_kelime[i + 1:]
                                                                                # Burada string  immutable ifade olmasından dolayı tahmini doğru yerine str toplama ile ekledim.
                if yapilan_tahmin in sesli_harfler:
                    puan += 3*kac_kere_var
                else:
                    puan += 2*kac_kere_var
                if "-" not in bilinmeyen_kelime:                                                            # Kelime içerisinde "-" ifadesi kalmadıysa kelime doğru bilinmiştir.
                    print("""
                          »»————-　★　————-««
                      TEBRİKLER KELİMEYİ BULDUNUZ      
                      Şuanki drumda kelime: '{}'
                      Puan drumunuz:{} 
                          »»————-　★　————-««
                            """.format(kelime,puan))
                    break
                print("""
                      ---------------------------
                      TEBRİKLER DOĞRU TAHMİN 
                      Şuanki drumda kelime: '{}'
                      Puan drumunuz:{} 
                      ------------------------------"""
                      .format(bilinmeyen_kelime, puan))                                                                 # "-" ifadesini kontrol ettikten sonra hala var ise
            else:                                                                                  # oyun devam etmeli. Bu sebepten sonradan doğru tahmin olduğunu belirttim.
                tahminHak -= 1                                                                                          # yapılan tahmin doğru değilse else bloğu çalışıyor.
                puan -= 4
                if tahminHak == 0:
                    print("""\t\t\t\t\tTahmin hakkınız bitti.
                                   Puanınız: {} 
                                   Kelime :"{}" olmalıydı.""".format(puan, kelime))
                    break
                print("""
                     *************************
                     Yanlış tahminde bulundunuz...
                     Kalan tahmnin hakkınız:{}
                     Puan drumunuz: {}
                     ***************************
                  """.format(tahminHak, puan))
