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
### Img
### positive.txt
### negative.txt
### vector.bat
### train.bat

'Img' klasörü altında 'positive' ile 'negative' dosyaları bulunmaktadır. 'positive' kısmında eğitimi yapılacak objeye ait resim eklendi. (Mevcut resim üzerinden ilerlendi.)
'negative' kısmında ise objenin olmadığı resimler eklendi. İlk başta bulmasını istediğim objeyi PS yardımı ile sildim ve ilk eğitimlerime başladım.
Opencv kütüphanesinde bulunan 'opencv_createsamples' ile mevcut resim üzerinden eğitimi yapılacak objeye ait resmin farklı boyutlarda birden fazla pozitif resmini işleyebilmesi için vektör'e çevrilme işlemi gerçekleşti.
'opencv_traincascade' ile ise vektöre çevrilen pozitif objelerin ve negatif objelerin verilmesi ve eğitim için gereken parametrelerin girilmesi ile eğitim sonuçlandı.(Standart değerler)


# PYTHON SURUM
### 3.9.4

# OPENCV SURUM
### 4.5.4.58
