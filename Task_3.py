text = input()

textSymbolsCod = []
textValues = 0

for letter in text:
    textValues = int(ord(letter))
    textSymbolsCod.append(textValues)

print('Sum of cod symbols in text = ', sum(textSymbolsCod))