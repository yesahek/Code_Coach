word = input()
vowels = ("a", "e", "i", "u", "o")
#words = list(word)
res = [i for i in word if i not in vowels]
print(res)
