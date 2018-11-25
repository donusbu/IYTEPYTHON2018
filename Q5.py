i = 2
sayı = int(input("Bir sayi giriniz: "))
liste=[]
çarpan=[]

while i < sayı:
    if (sayı % i == 0):
        print(i)
        liste.append(i)
    i += 1
del i

print(liste)

for i in liste:
    sonlandir = True
    for a in liste:
        if (sonlandir):
            if(i == a):
                çarpan.append(i)
            elif(i%a == 0):
                sonlandir = False

'''Yazdigim program tam olarak sizin istediginiz sekilde calismiyor. 16'nin tum asal bolenlerini yazmak yerine 16'yi
bolebilen tum sayilari basiyor.'''