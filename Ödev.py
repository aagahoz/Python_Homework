import time
def İkiSayı():
    first = input("İlk Sayıyı Yazınız: ")
    second = input("İkinci Sayıyı Yazınız: ")
    if first.isnumeric() and second.isnumeric():
        result = max(int(first),int(second))
        print("Büyük Sayı: ",result)
    else:
        print("Hatalı Giriş, Sadece Sayılar Büyükten Küçüğe Sıralanabilir!")

def ÜcSayı():
    first = input("İlk Sayıyı Yazınız: ")
    second = input("İkinci Sayıyı Yazınız: ")
    third = input("Üçüncü Sayıyı giriniz: ")
    if first.isnumeric() and second.isnumeric() and third.isnumeric():
        result = max(first,second,third)
        print("Büyük Sayı: ",result)
    else:
        print("Hatalı Giriş, Sadece Sayılar Büyükten Küçüğe Sıralanabilir!")

def onbeş():
    number = input("Sayıyı giriniz: ")
    if number.isnumeric():
        number = int(number)
        if number % 5 == 0 and number % 3 == 0:
            print("Sayı 15 e Tam bölünür.")
        else:
            print("15 e bölünemez")
    else:
        print("Hatalı giriş,Sadece Sayı Girin!")

def asalBulma():
    liste = []
    for sayı in range(100):
        if sayı > 1:
            for i in range(2,sayı):
                if sayı % i == 0:
                    break
            else:
                liste.append(sayı)
    print(liste)

def eslestirme():
    liste1 = []
    liste2 = []
    baslangıc = 0
    while(baslangıc<5):
        ekle1 = input("Liste 1 için sayı giriniz: ")
        ekle2 = input("Liste 2 için sayı giriniz: ")
        liste1.append(ekle1)
        liste2.append(ekle2)
        baslangıc += 1
    esListe = list(zip(liste1,liste2))
    print(esListe)

class KümeSınıfı():
    def __init__(self):
        print("Küme Oluşturuldu!")
        self.isim = "isim"
        self.icerik = []
    def eleman_bastır(self):
        print("Elemanlar: ",self.icerik)
    def eleman_ekle(self,eleman):
        self.eleman = eleman
        self.icerik.append(int(eleman))
        print("eleman eklendi",int(eleman))
    def eleman_sayısı (self):
        print(len(self.icerik))
    def altküme_sayısı(self):
        print(2**(len(self.icerik)))
    def özaltküme_sayısı(self):
        print(2**len(self.icerik)-1)
    def küme_birleştir(self):
        küme_birlesim = KümeSınıfı()
        print("Çözülemeyen Soru 1")
        pass
    def küme_kesiştir(self):
        küme_kesişim = KümeSınıfı()
        print("Çözülemeyen Soru 2")
        pass
def program_baslat():
    print("""
    *************************
    Program Başlatıldı...

    İşlemler:
    1. Alınan 2 sayıdan büyük olanı bastırma
    2. Alınan 3 sayıdan en büyük olanı bastırma
    3. 15 e bölünebilen sayı bulma 
    4. 0 - 100 arası asal sayıları bastırma 
    5. 2 Listenin elemanlarını eşleştirme
    6. Küme sınıfı ile ilgili işlemler
    7. Bu soruyu şimdilik boşver..
    Çıkmak İçin 'q' yazınız.
    ***************************""")
    while(True):
        islem = input("Yapmak İstediğiniz İşlemin Numarasını Giriniz: ")
        if islem == 'q':
            break
        elif islem ==  '1':
            İkiSayı()
        elif islem == '2':
            ÜcSayı()
        elif islem == '3':
            onbeş()
        elif islem == '4':
            asalBulma()
        elif islem == '5':
            eslestirme()
        elif islem == '6':
            küme_adı1 = input("Küme Adı Giriniz:")
            küme_adı1 = KümeSınıfı()
            küme_adı2 = input("2. Bir Küme Oluşturup İşlem Yapacaksanız lütfen Küme Adı Giriniz, Yapmayacaksanız 'hayır' yazınız:")
            küme_birlesim = KümeSınıfı()

            if küme_adı2 == 'hayır':
                print("2. Küme Oluşturulmadı")
                pass
            else:
                küme_adı2 = KümeSınıfı()
            while(True):
                print("""
                Yapılabilecek İşlemler:
                    1. Kümeye Eleman Eklemek
                    2. Küme Elemanlarını Yazdırmak
                    3. Kümenin Eleman Sayısını Yazdırmak
                    4. Kümenin Altküme Sayısını Yazdırmak
                    5. Kümenin ÖzaltKüme Sayısını Yazdırmak
                    6. İki Kümeyi Birleştirip Yeni Bir Küme Oluşturmak
                    7. İki Kümenin Kesişiminden Yeni Bir Küme Oluşturmak
                    Küme İslemini bitirmek ve kümeyi silmek için 'sil' yazınız
                """)
                islem2 = input("Küme İşlem Numarasını Giriniz: ")

                if islem == 'sil':
                    break
                elif islem2 == '1':
                    girilen = input("Elemanı Yaz: ")
                    küme_adı1.eleman_ekle(girilen)
                elif islem2 == '2':
                    küme_adı1.eleman_bastır()
                elif islem2 == '3':
                    küme_adı1.eleman_sayısı()
                elif islem2 == '4':
                    küme_adı1.altküme_sayısı()
                elif islem2 == '5':
                    küme_adı1.özaltküme_sayısı()
                elif islem2 == '6':
                    küme_adı1.küme_birleştir()
                elif islem2 == '7':
                    küme_adı1.küme_kesiştir()
                else:
                    print("Hatalı İşlem Seçimi")
                time.sleep(1.5)
        elif islem == '7':
            print("Çözülemeyen Soru")
        else:
            print("Hatalı Giriş!")
        time.sleep(1.5)
program_baslat()
