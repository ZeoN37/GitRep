number_1 = 3
number_2 = 6

while True:
    operation = input('Bедите операцию:')
    try:
        operation == '+'
        result = number_1 + number_2
        print(f'{number_1}+{number_2}={result}')
        break

    except ValueError:
        try:
            operation == '-'
            result = number_1 - number_2
            print(f'{number_1}-{number_2}={result}')
            break

        except ValueError:
            try:
                operation == '*'
                result = number_1 * number_2
                print(f'{number_1}*{number_2}={result}')
                break

            except ValueError:
                print("Неверное значение. Bедите второе число: ")
