
def exe_2(**kwargs):
    kwargs = {"name": input('Enter name: '),
              "s_name": input('Enter second name: '),
              "b_date": input('Enter birth day: '),
              "l_town": input('Enter live town: '),
              "email": input('Enter email: '),
              "tel": input('Enter tel number: ')}
    return ' '.join(kwargs.values())
print(exe_2())

