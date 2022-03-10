print("░P░y░t░h░o░n░ ░H░e░s░a░p░ ░M░a░k░i░n░e░s░i░")

devam_etmek_istiyormusunuz=int(input("Devam etmek isityormusunuz?: \n 0: Çıkış \n 1: Devam et \n : "))


if devam_etmek_istiyormusunuz==1:
    ana = int(input(" İşlemler: \n 1: Toplama \n 2: Çıkarma \n 3: Çarpma \n 4: Bölme \n 5: M2 Hesaplama (Alan Hesaplama) \n 6: Çevre Hesaplama \n 7: Daire Çevre Hesaplama \n 8 : Daire Alan Hesaplama \n 9: Üçgen Çevresi Hesaplama \n 10: Üçgen Alanı Hesaplama \n 11: Yüzdelik Dilim Hesaplama \n : " ))



    if ana == 1:
        a = float(input("ilk sayı: "))
        b = float(input("ikinci sayı: "))
        print("Sonuç", a + b)

    elif ana == 2:
        a = float(input("ilk sayı: "))
        b = float(input("ikinci sayı: "))
        print("Sonuç", a - b)

    elif ana == 3:
        a = float(input("ilk sayı: "))
        b = float(input("ikinci sayı: "))
        print("Sonuç", a * b)

    elif ana == 4:
        a = float(input("ilk sayı: "))
        b = float(input("ikinci sayı: "))
        print("Sonuç", a / b)

    elif ana == 5:
        a = float(input("Kenar: "))
        b = float(input("2.Kenar: "))
        print("sonuç", a * b, "metrekare")

    elif ana == 6:
        a = float(input("ilk kenar: "))
        b = float(input("ikinci kenar: "))
        e = float(input("üçuncü kenar: "))
        f = float(input("Dördüncü kenar: "))
        c = a + b + e + f
        print("sonuç", c, "metre")

    elif ana == 7:
        a = float(input("çap: "))
        b = float(input("pi sayısı: "))
        c = a * b
        print("sonuc", 2 * c, "metrekare")

    elif ana == 8:
        a = float(input("çap: "))
        b = float(input("pi sayısı: "))
        c = a * a
        print("sonuç", b * c, "metrekare")

    elif ana == 9:
        a = float(input("ilk kenar: "))
        b = float(input("ikinci kenar: "))
        e = float(input("üçuncü kenar: "))
        c = a + b + e
        print("sonuc", c, "metre")

    elif ana == 10:
        a = float(input("taban: "))
        b = float(input("yükseklik: "))
        c = a * b / 2
        print("sonuç", c, "metrekare")

    elif ana == 11:
        a = float(input("Sayı: "))
        b = float(input("Yüzdelik: "))
        print("sonuç", a * b / 100)
