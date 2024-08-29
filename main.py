from math import trunc

def main(ex):
    example = check(ex)

    if not (example):
        return None

    if example[1] == '+':
        print(int(example[0]) + int(example[-1]))
    elif example[1] == '*':
        print(int(example[0]) * int(example[-1]))
    elif example[1] == '-':
        print(int(example[0]) - int(example[-1]))
    else:
        print(trunc(int(example[0]) / int(example[-1])))

def check(ex):
    ex = ex.split()

    if len(ex) != 3:
        print('throws Exception')
        return False

    if not (ex[0].isdigit() and ex[-1].isdigit()):
        print('throws Exception')
        return False

    if not (1 <= int(ex[0]) <= 10 and 1 <= int(ex[-1]) <= 10):
        print("throws Exception")
        return False

    if ex[1] not in ['+', '-', '*', '/']:
        print('throws Exception')
        return False

    return ex

while True:
    main(input())