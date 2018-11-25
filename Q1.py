#Gecen hafataki kodlari yazdir.


array = [1, 2, 3, 4, 5, 6, 7, 8]
for item in array:
	print(array)

#max
array = range( 1, 8 )
max_ = array[0]
 for data in array:
 	if max_ < data:
 		max_ = data
print(max_)


# map
array = [1, 2, 3, 4, 5, 6]
newArray = []
for item in array:
newArray.append(item + 2)

print(newArray)


# reduce
array = [1, 2, 3, 4, 5, 6, 7, 8]
total = 0.0
for item in array:
 	total = total + item

print(total)

# filter
array = [1, 2, 3, 4, 5, 6, 7, 8]
newArray = []

for data in array:
    if data % 2 == 0:
 		newArray.append(data)
print(newArray)



text = 'merhaba'
newList = []
for char in text:
    newList.append(chr(ord(char) - 32))
newText = ''.join( newList )



while True:
 	print('Bunu sonsuza kadar yaz.')

i = 0
while i < 10:
 	print(i)
 	i += 1

i = 0
while i < 10:
 	print(i)
 	if i == 4:
 		break
 	i += 1

sayi = int(input('Bir sayi giriniz:'))
baslangic = 2
asal_mi = True
while baslangic < sayi:
    if sayi % baslangic == 0:
 		asal_mi = False

if asal_mi:
 	print('Sayi asaldir.')
else:
 	print('Sayi asal degildir.')

