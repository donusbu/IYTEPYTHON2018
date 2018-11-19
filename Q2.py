text = input("Bir text giriniz:")
text.split()
reverse = reversed(text)
new_text = ''.join(reverse)

if text == new_text:
    print("Bu text palindromdur.")
else:
    print("Bu text palindrom değildir.")