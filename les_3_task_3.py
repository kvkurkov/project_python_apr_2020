def my_func(arg_1, arg_2, arg_3):
    args = [arg_1, arg_2, arg_3]
    res = []
    args.remove(min(args))
    res.extend(args)
    return sum(res)


print(f'Result - {my_func(int(input("first arg ")), int(input("second arg ")),int(input("third arg ")))}')
