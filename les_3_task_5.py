def exe_5():
    res = 0
    while True:
        num = input('Enter list of number or # to exit: ').split()
        for i in num:
            try:
                if i == '#':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Enter number or #')
        print(f'Sum is {res}')

print(exe_5())