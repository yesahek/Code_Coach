text = input()

text = text.split()
length = [len(x) for x in text]
maxLength = max(length)
maxLengthIndex = length.index(maxLength)
print(text[maxLengthIndex])
