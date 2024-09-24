def main(example):
    example = example.split()

    if len(example) != 3:
        return 'Введено невалидное значение'

    if example[1] not in ['+', '-', '*', '/']:
        return 'Некорректная математическая операция'

    try:
        if not (1 <= int(example[0]) <= 10) or not (1 <= int(example[-1]) <= 10):
            return 'Нарушено условие ввода чисел'
    except Exception as ex:
        return ex

    if example[1] == '+':
        return int(example[0]) + int(example[-1])
    elif example[1] == '*':
        return int(example[0]) * int(example[-1])
    elif example[1] == '-':
        return int(example[0]) - int(example[-1])
    else:
        return int(example[0]) // int(example[-1])

