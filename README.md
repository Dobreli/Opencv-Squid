# Squid 
### cascade 
cascade kısmında eğitimi tamamlanmış xml dosyalarım bulunmaktadır.
### traincascade
traincascade kısmında her bir obje için eğitimler ve aşamaları bulunmaktadır.

Her bir obje içerisinde 'Cascade','Img','Out','TestCascade' dosyaları bulunmaktadır.

'Cascade' kısmında en son yapmış olduğum eğitim çıktısı bulunur.
'Img' kısmında pozitif ve negatif resimlerimin bulunduğu kısımdır.
'TestCascade' kısmında ise daha önce yapmış olduğum eğitimlerdir.
'Out' kısmında ise her eğitim sonrası tespit ettiği objelerin birer kopyasını kayıt ettiği kısımdır. </br>

# train.py
Burada en iyi sonuca ulaşana kadar bu döngü tekrarlanmış ve 'TestCascade' kısmına çıktısı kayıt edilmiştir.</br>
Her eğitim sonrası 'Out' dosyasında kayıt edilen resimler arasından yanlış olarak tespit ettilerini 'Img' içerisinde 'negative' kısmına eklenerek ve doğru olarak bulduğundan emin olduğum çıktının konum bilgileri 'positive.txt' dosyasına eklenerek 'TestCascade' içerisindeki 'Final' eğitimine ulaşılmıştır.

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
'positive.txt' belgesine verilen yolları alıp her resmi vektör biçimine çevirir ve 'el.vec' kayıt eder. Bunu Opencv kütüphanesinde bulunan 'opencv_createsamples' ile gerçekleştirilir. 
-info positive.txt : </br>
-num 600 :  Toplam pozitif değer </br>
-vec el.vec : Çıktı ismi </br>
-w 24 -h 24  : İşlem boyutu </br>


### el.vec
'opencv_createsamples'  çıktısıdır.

### train.bat
'opencv_traincascade' ile eğitim gerçekleşti. </br></br>
-data Cascade : kayıt edilecek dosya </br>
-vec el.vec : 'vector.bat' ile dönüştürdüğümüz pozitif veri çıktısı. </br>
-bg negative.txt : 'negative.txt' belgesi </br>
-numNeg 60 : Toplam negatif veri  </br>
-numStages 5 : Eğitim adım sayısı </br>
-minHitRate 0.995 : Minimum yaklaşım değeri (standart)</br>
-maxFalseAlarmRate 0.2 : hata değeri (standart)</br>
-w 24 -h 24 : işlem yapılacak boyut </br>
-numPos hesaplaması: </br>
toplam_pozitif_değer-toplam_negatif_deger / 1(eğitim_adım_sayısı-1)x(1-minimum yaklaşım değeri)


# PYTHON SURUM
### 3.9.4

# OPENCV SURUM
### 4.5.4.58
