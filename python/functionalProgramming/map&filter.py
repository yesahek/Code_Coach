names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

#your code goes here
res = list(filter(lambda x: len(x) > 4, names))
print(res)
