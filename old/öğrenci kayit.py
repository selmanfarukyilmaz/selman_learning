

def ortalamalari_oku ():
    pass

def not_gir():
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci SoyAdı: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")

    with open ("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"/n")

def notlari_kayit_et():
    pass

while True:
    islem = input("1- Notları Oku/n2- Not Gir/3- Notları Kayıt Et /4- Çıkış/n")

    if islem == "1":
        ortalamalari_oku()
    elif islem =="2":
        not_gir()
    elif islem == "3":
        notlari_kayit_et()
    else:
        break