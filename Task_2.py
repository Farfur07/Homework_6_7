inputName = input()


for item in inputName:
    digit = 0
    if item.isdigit() and digit >= 0:
        print('Wrong enter - remove numbers from text')
    else:
        if not item.isdigit():
            continue

inputNameFormat = inputName.title()
print(inputNameFormat)
