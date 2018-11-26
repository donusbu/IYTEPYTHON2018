text_1 = input("Bir metin giriniz: ")
text_2 = input("Bir metin daha giriniz: ")

if set(text_1.split(" ")) & set(text_2.split(" ")):
    print("Bu text ilk textin icinde geciyor.")
else:
    print("Bu text ilk textin icinde gecmiyor.")









