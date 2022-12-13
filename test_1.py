operation = input('Bедите операцию:')
if operation == str("+"):
    result_1 = number_1 + number_2
    print(f'{ number_1 }+{number_2}={ result_1 }')
elif operation == str("-"):
    result_1 = number_1 - number_2
    print(f'{number_1}-{number_2}={result_1}')
elif operation == str("*"):
    result_1 = number_1 * number_2
    print(f'{number_1}*{number_2}={result_1}')
else:
    print(f'Неизвестная операция')