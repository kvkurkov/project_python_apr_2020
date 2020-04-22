my_rating = [6, 8, 9, 3, 5]
user_var = int(input("введите число"))
for el in my_rating:
    if user_var == el:
        j = my_rating.index(el)
        my_rating.insert(j,user_var)
    else:
        my_rating.append(user_var)
        break
print(my_rating)
