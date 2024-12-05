num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите тип операции (+, -, *, /, **): ")

result = None

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2
    case '**':
        result = num1 ** num2

print(result)