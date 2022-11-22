txt = input()


def words(x):
    # your code goes here
    li = x.split(" ")
    for i in li:
        yield i


print(list(words(txt)))
