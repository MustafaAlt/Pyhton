
# Sayı Tabanı Dönüştürücü (Binary & Decimal)

Bu Python projesi, kullanıcıya 10'luk (decimal) sayı sisteminden 2'lik (binary) sayı sistemine ve tam tersine dönüştürme imkanı sunar. Program sonsuz döngü içerisinde çalışır ve kullanıcı çıkmak isteyene kadar işlemleri tekrar eder.

## 🧠 Özellikler

- 10'luk tabandan 2'lik tabana dönüştürme (pozitif ve negatif sayılar dahil)
- 2'lik tabandan 10'luk tabana dönüştürme
- Geçersiz girişlerde kullanıcıya uyarı verilir
- Kullanıcı çıkış yapana kadar program çalışmaya devam eder

## 📌 Kullanım

Program çalıştırıldığında şu menü ile karşılaşırsınız:

```
     1-) 10'luk tabandan 2'lik tabana çevirme 
     2-) 2'lik tabandan 10'luk tabana çevirme 
     3-) Çıkış
```

### 1️⃣ 10'luk Tabandan 2'lik Tabana

Kullanıcıdan bir sayı alınır. Sayı negatifse, sonuç başına `1` eklenerek işaretlenir ve binary karşılığı terslenerek gösterilir. Örnek çıktı:

```
Lütfen 2'lik tabana çevirmek istediğiniz sayıyı giriniz: -6
(-6)₁₀ = (110)₂
```

### 2️⃣ 2'lik Tabandan 10'luk Tabana

Kullanıcıdan binary formatta bir sayı alınır. Sayı kontrol edilir ve geçerli değilse uyarı verilir. Örnek çıktı:

```
Lütfen 10'luk tabana çevirmek istediğiniz sayıyı giriniz: 1101
(1101)₂ = (13)₁₀
```

### 3️⃣ Çıkış

Programdan çıkış yapar.

## 🧑‍💻 Geliştirici

**Mustafa Altiparmak**  
Öğrenci No: 21100011032

## 📄 Lisans

Bu proje eğitim amaçlıdır ve serbestçe kullanılabilir.
