yil = input("Bir yil giriniz: ")

if yil.isdigit():
    yil = int(yil)
    print(yil)
else:
    yil.isdigit()
    print("Girdiğiniz değer tanımlanamadı.")

yil = int(input("Bir yil giriniz: "))
if yil % 4 != 0 or (yil % 100 == 0 and yil % 400 != 0):
    print("Bu bir artik yil degildir.")
else:
    print("Bu bir artik yildir.")