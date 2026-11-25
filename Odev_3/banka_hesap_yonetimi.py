class Hesap: # Hesap sınıfı oluşturuldu
    def __init__ (self, musteri_ismi, hesap_no, bakiye): # Hesap sınıfının başlatıcı fonksiyonu oluşturuldu
        self.musteri_ismi = musteri_ismi # Müşteri ismi atanıyor
        self.hesap_no = hesap_no # Hesap numarası atanıyor
        self.bakiye = bakiye # Bakiye atanıyor

    def para_yatirma(self, miktar): # Para yatırma fonksiyonu oluşturuldu
        if miktar > 0: # Eğer miktar 0'dan büyükse
            self.bakiye += miktar # Bakiye yatırılan miktara göre değişiyor
            print(f"{miktar} yatırıldı. Yeni bakiye : {self.bakiye} ") # Yatırılan miktar ve yeni bakiye ekrana yazdırılıyor
        else: # Aksi durumda
            print("Lütfen geçerli bir miktar giriniz") # Geçersiz miktar için hata mesajı ekrana yazdırılıyor

    def para_cekme (self, miktar): # Para çekme fonksiyonu oluşturuldu
        if miktar > 0 and miktar <= self.bakiye: # Eğer miktar 0'dan büyük ve bakiyeden küçükse
            self.bakiye -= miktar # Bakiye çekilen miktara göre değişiyor
            print(f"{miktar} çekildi. Yeni bakiye : {self.bakiye}") # Çekilen miktar ve yeni bakiye ekrana yazdırılıyor
        else: # Aksi durumda
            print("Yetersiz bakiye ya da geçersiz miktar! Lütfen geçerli bir miktar giriniz.") # Geçersiz miktar için hata mesajı ekrana yazdırılıyor

    def bakiye_goruntuleme (self): # Bakiye görüntüleme fonksiyonu oluşturuldu
        print(f"{self.musteri_ismi} isimli müsterinin bakiyesi : {self.bakiye}") # Müşteri ismi ve bakiyesi ekrana yazdırılıyor
    
input_musteri_ismi = input("Müşteri ismini giriniz: ") # Müşteri ismi alınıyor
input_hesap_no = input("Hesap numarasını giriniz: ") # Hesap numarası alınıyor
input_bakiye = float(input("Başlangıç bakiyesini giriniz: ")) # Başlangıç bakiyesi alınıyor

hesap = Hesap(input_musteri_ismi, input_hesap_no, input_bakiye) # Hesap nesnesi oluşturuluyor
while True: # Sonsuz döngü oluşturuluyor
    print("1. Para Yatırma") # Para yatırma seçeneği ekrana yazdırılıyor
    print("2. Para Çekme") # Para çekme seçeneği ekrana yazdırılıyor
    print("3. Bakiye Görüntüleme") # Bakiye görüntüleme seçeneği ekrana yazdırılıyor
    print("4. Çıkış") # Çıkış seçeneği ekrana yazdırılıyor

    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1-4): ") # Kullanıcıdan seçim alınıyor

    if secim == "1": # Eğer müşteri 1'i seçerse
        miktar = float(input("Yatırmak istediğiniz miktarı giriniz: ")) # Yatırılacak miktar alınıyor
        hesap.para_yatirma(miktar) # Para yatırma fonksiyonu çağrılıyor
    elif secim == "2": # Eğer müşteri 2'yi seçerse
        miktar = float(input("Çekmek istediğiniz miktarı giriniz: ")) # Çekilecek miktar alınıyor
        hesap.para_cekme(miktar) # Para çekme fonksiyonu çağrılıyor
    elif secim == "3": # Eğer müşteri 3'ü seçerse
        hesap.bakiye_goruntuleme() # Bakiye görüntüleme fonksiyonu çağrılıyor
    elif secim == "4": # Eğer müşteri 4'ü seçerse
        print("Çıkış yapılıyor...") # Çıkış mesajı ekrana yazdırılıyor
        break # Döngüden çıkılıyor
    else: # Eğer müşteri geçersiz bir seçim yaparsa
        print("Geçersiz seçim! Lütfen tekrar deneyiniz.") # Hata mesajı ekrana yazdırılıyor