#тест
while True:
    number_1 = input('Bедите первое число: ')
    try:
        number_1 = int(number_1)
        print("Первое число: ", number_1)
        break
    except ValueError:
        try:
            float(number_1)
            print("Первое число: ", number_1)
            break
        except ValueError:
            print("Неверное значение. Bедите первое число: ")

while True:
    number_2 = input('Bедите второе число: ')
    try:
        number_2 = int(number_2)
        print("Второе число: ", number_2)
        break
    except ValueError:
        try:
            float(number_2)
            print("Второе значение: ", number_2)
            break
        except ValueError:
            print("Неверное значение. Bедите второе число: ")

while True:
    operation = input('Bедите операцию: ')
    try:
        if operation == '+':
            result = number_1 + number_2
            print(f'{number_1}+{number_2}={result}')
            break
        if operation == '-':
            result = number_1 - number_2
            print(f'{number_1}-{number_2}={result}')
            break
        if operation == '*':
            result = number_1 * number_2
            print(f'{number_1}*{number_2}={result}')
            break
        if operation == '/':
            result = number_1 / number_2
            print(f'{number_1}/{number_2}={result}')
            break
        else:
            print("Неверное значение. Bедите операцию: ")
    except ValueError:
        continue



