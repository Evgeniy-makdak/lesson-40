def decorate_method(method):
    def inner(*args, **kwargs):
        dict_numbers = {str(x): x for x in range(1, 6)}
        dict_numbers.update({'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5})

        if type(args[1]) == str:
            if args[1] in dict_numbers:
                other = dict_numbers[args[1]]
                args = [args[0], other]
                return method(*args, **kwargs)
            raise TypeError('справа от знака "+" некорректные символы. Введите цифры в диапазоне от 1 до 5.')
        return method(*args, **kwargs)
    return inner


class Int(int):

    @decorate_method
    def __add__(self, other):
        return super().__add__(other)

if __name__ == '__main__':
    # демонстрация работы
    x = Int(3)
    print(x + '5')  # 8
    print(x + 'один')  # 4
    print(x + 'три')  # 6
    print(x + 'одиннадцать')  # TypeError: справа от знака "+" некорректные символы. Введите цифры в диапазоне от 1 до 5.
    # print(x + 'a')  # TypeError: справа от знака "+" некорректные символы. Введите цифры в диапазоне от 1 до 5.
    # print(x + (1,))  # TypeError: unsupported operand type(s) for +: 'Int' and 'tuple'