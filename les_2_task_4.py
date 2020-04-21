var_1 = input("Введите слова через пробел")
var_2 = var_1.split()

for ind, el in enumerate(var_2, 1):
    if len(el) > 10:
        print(ind, el[:10])
    else:
        print(ind,el)