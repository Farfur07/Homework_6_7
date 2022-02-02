
text = input()

text = text.split()

boxOfTextLen = []

for textLen in text:
    textLen = len(textLen)
    if textLen >= 0:
        boxOfTextLen.append(textLen)
        print(boxOfTextLen)

print(max(boxOfTextLen))

