word = 'hero'
for letter in word:
    if letter == 'x':
        print("Eak! An 'x'!")
        break
    print(letter)
else:
        print("No 'x' in word")