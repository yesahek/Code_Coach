file = open("books.txt", "r")

# your code goes here
lines = file.readlines()
count = 1
for i in lines:
    fc: str = i[0]
    n = len(lines)
    if count != n:
        ll = str(len(i) - 1)
        print(fc + ll)
        # print(n)
        # print(count)
        count = + count + 1
    elif count == n:
        ll = str(len(i))
        print(fc + ll)
        # print("else")

file.close()
