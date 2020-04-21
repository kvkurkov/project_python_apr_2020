month = int(input("введите номер месяца"))
season_name = ["зима",
               "весна",
               "лето",
               "осень"]
if month <= 12:
    season_index = month // 3 % 4
    print(season_name[season_index])
else:
    print("Ошибка, введите номер месяца от 1 до 12")
seasons_dict = {"зима": (12, 1, 2),
                "весна": (2, 4, 5),
                "лето": (6, 7, 8),
                "осень": (9, 10, 11)}
for key, value in seasons_dict.items():
    if month in value:
        print(key)
        break
