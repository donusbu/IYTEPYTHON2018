text_1 = "Bu cümlede 4 elma 5 armut 8 tane de muz var"
print(text_1)
words = text_1.split(" ")  # bu cumleyi yani text_1 degiskenini bosluklara gore ayirdik
newArray = words[:]
print(words)

for element in words:  # for loop ile kelimeleri geziyoruz ve array'in her bir elemanini ekrana basiyoruz
    try:
        element = int(element)
        print(element)
    except ValueError:
        newArray.remove(element)

print(newArray)
number1 = ""
for number in newArray:
    number1 = number1 + number  # tum rakamlar gezildi ve number1 string'ine eklendi

print(int(number1))

text_2 = "bu ikinci cümlede 9 kiraz 3 karpuz var"
words2 = text_2.split(" ")
newArray2 = words2[:]
print(words2)
for n2 in words2:
    try:
        n2 = int(n2)
        print(n2)
    except ValueError:
        newArray2.remove(n2)

print(newArray2)
number2 = ""  # Define a string.
for num in newArray2:
    number2 = number2 + num

print(number2)
print(int(number1) + int(number2))