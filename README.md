# Squid 
### cascade 
cascade kısmında eğitimi tamamlanmış xml dosyalarım bulunmaktadır.
### traincascade
traincascade kısmında her bir obje için eğitimler ve aşamaları bulunmaktadır.

Her bir obje içerisinde 'Cascade','Img','Out','TestCascade' dosyaları bulunmaktadır.

'Cascade' kısmında en son yapmış olduğum eğitim çıktısı bulunur.
'Img' kısmında pozitif ve negatif resimlerimin bulunduğu kısımdır.
'TestCascade' kısmında ise daha önce yapmış olduğum eğitimlerdir.
'Out' kısmında ise her eğitim sonrası tespit ettiği objelerin birer kopyasını kayıt ettiği kısımdır.
Her eğitim sonrası 'Out' dosyasında kayıt edilen resimler arasından yanlış olarak tespit ettilerini 'Img' içerisinde 'negative' kısmına eklendi.

# Eğitim

### Cascade
'train.bat' xml çıktısı bu dosyaya kayıt edilmektedir. 

### Img
'Img' klasörü altında 'positive' ile 'negative' dosyaları bulunmaktadır. 'positive' kısmında eğitimi yapılacak objeye ait resim eklendi. (Mevcut resim üzerinden ilerlendi.)
'negative' kısmında ise objenin olmadığı resimler eklendi. (İlk başta bulmasını istediğim objeyi PS yardımı ile sildim ve ilk eğitimlerime başladım.)

### positive.txt
'Img' klasörü altında bulunan 'positive' klasörü içindeki objeye ait resimin/lerin dosya yollarının yazıldığı belge. Burda her resim içinde objeden kaç tane olduğu ve nerede olduğu dosya yolunun hemen yanına (x,y,w,h formatında) eklendi.

### negative.txt
'Img' klasörü altında bulunan 'negative' klasörü içindeki objeye ait olmayan resimin/lerin dosya yollarının yazıldığı belge.

### vector.bat
'positive.txt' belgesine verilen yolları alıp her resmi vektör biçimine çevirir ve 'el.vec' kayıt eder. Bunu Opencv kütüphanesinde bulunan 'opencv_createsamples' ile gerçekleştirilir. (girdi: 'positive.txt' belgesi, kaç adet veri olduğu, hangi isimde kayıt edileceği)

### el.vec
'opencv_createsamples'  çıktısıdır.

### train.bat
'opencv_traincascade' ile eğitim gerçekleşti.
-numpos hesaplaması:
positif_değer-negatif_deger
___________________________
1(eğitim_adım_sayısı-1)x(1-minimum yaklaşım değeri)


# PYTHON SURUM
### 3.9.4

# OPENCV SURUM
### 4.5.4.58
