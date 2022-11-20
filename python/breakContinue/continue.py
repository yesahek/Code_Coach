total = 0
#your code goes here
i =0
while i < 5:
    text = int(input())
    if text >= 5:
        i += 1
        total = total + 100
    else:
        i = i + 1
        continue
print(total)
