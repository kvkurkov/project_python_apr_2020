def div_func():
    try:
        dividend = float(input("Введите делимое: "))
        divider = float(input("Введите делитель: "))
        res = dividend/divider
        return (res)
    except ValueError:
        return("Ошибка ввода")

    except ZeroDivisionError:
        return("Ошибка деления на 0")
print(div_func())


