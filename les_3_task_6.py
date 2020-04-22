def int_func(*args):
    args = str(args)
    return args.title()


print(int_func(str(input('input words: '))))
