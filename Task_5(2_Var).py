text = input()
text = text.split()

longestString = max(text, key=len)

print(longestString)