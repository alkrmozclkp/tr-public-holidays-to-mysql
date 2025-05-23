# tr-public-holidays-to-mysql
Bu Python projesi, Türkiye'ye ait resmi tatil günlerini otomatik olarak alır ve bir MySQL veritabanına kaydeder. Tatiller, mevcut yıldan itibaren 10 yıl boyunca çekilir.
##  Özellikler
- `holidays` kütüphanesini kullanarak Türkiye tatillerini alır.
- MySQL veritabanına kayıt yapar.
- Mükerrer (aynı tarih ve isimdeki) kayıtları engeller.
- Her yıl için tekrar çalıştırmaya uygundur.
## Kullanılan Teknolojiler
- Python
- MySQL Sunucusu
- `pip` paket yöneticisi
- (Opsiyonel) Docker