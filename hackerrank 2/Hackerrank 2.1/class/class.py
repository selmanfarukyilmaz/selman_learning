class Calisan:
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"

    def bilgileri_göster(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} Maaş:{self.maas} Email: {self.email} "


calisan1 = Calisan("Ali", "Çalışkan", 5000)
calisan2 = Calisan("Veli", "Uzun", 6000)


class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        super().__init__(isim, soyisim, maas)
        self.bildigi_dil = bildigi_dil

    zam_orani = 1.2

    def bilgileri_göster(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} Maaş:{self.maas} Email: {self.email} Dil: {self.bildigi_dil} "

    def dilini_soyle(self):
        return f"Bildiğim dil: {self.bildigi_dil}"


yazilimci1 = Yazilimci("Ayşe", "Yıldız", 7000, "Python")
yazilimci2 = Yazilimci("Fatma", "Ay", 8000, "Java")


# print(yazilimci1.bilgileri_göster())
# print(yazilimci2.bilgileri_göster())
# print(yazilimci1.dilini_soyle())


class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, calisanlar=None):
        super().__init__(isim, soyisim, maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self, calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self, calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_göster())


yönetici1 = Yonetici("Metin", "Ali", 10000)

yönetici1.calisan_ekle(calisan1)
yönetici1.calisan_ekle(yazilimci1)
yönetici1.calisanlari_goster()
print("******")
yönetici1.calisan_sil(calisan1)
yönetici1.calisanlari_goster()

yönetici2 = Yonetici("Feyyaz", "Beşitaş", 11000, [yazilimci1, yazilimci2, calisan1])
yönetici2.calisanlari_goster()

# yönetici2 calısan classından üretilmiş bir nesne mi ?
print(isinstance(yönetici2, Calisan))

# Yazılımcı Calısan Class'ından türemiş midir ?
print(issubclass(Yazilimci, Calisan))
