metin = input("Lütfen bir cümle veya paragraf giriniz: ") # Bir cümle veya paragraf alıyoruz 

kucuk_metin = metin.lower()  # Büyük/küçük duyarlılığı olmaması için harfleri küçük harfe çeviriyoruz

kelime_listesi = kucuk_metin.split()  # Metni kelimelere ayırıyoruz 

print("Girilen metindeki kelimeler:", kelime_listesi) # Girilen metindeki kelimeleri ekrana yazdırıyoruz
print("Toplam kelime sayısı:", len(kelime_listesi)) # Girilen metindeki toplam kelime sayısını ekrana yazdırıyoruz
print("Toplam karakter sayısı (boşluklar dahil):", len(metin))  # Boşluklar dahil karakter sayısını yazdırıyoruz

en_uzun_kelime = 0
for kelime in kelime_listesi: # Kelimelere tek tek bakarak kontrol ediyoruz 
    if len(kelime) > en_uzun_kelime: # Eğer kelimenin uzunluğu en uzun kelimeden büyükse
        en_uzun_kelime = len(kelime) # En uzun kelimeyi güncelliyoruz

print("En uzun kelimenin uzunluğu:", en_uzun_kelime) # En uzun kelimenin uzunluğunu ekrana yazdırıyoruz

kelime_sayilari = {}
for kelime in kelime_listesi: # Kelimelere tek tek bakarak kontrol ediyoruz
    if kelime in kelime_sayilari: # Eğer kelime daha önceden yazılmışsa
        kelime_sayilari[kelime] += 1 # Kelimenin sayısını bir arttırıyoruz
    else : # Eğer kelime daha önceden yazılmamışsa
        kelime_sayilari[kelime] = 1 # Kelimenin sayısını 1 olarak başlatıyoruz

print("Kelime sayıları:", kelime_sayilari) # Kelime sayısını ekrana yazdırıyoruz