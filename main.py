print(" Калькулятор  ")
print("Пример : 2 + 3")

def main(input_str: str) -> str:
    a, b, c = input_str.split()
    a, c = int(a), int(c)

    if a > 10 or c > 10:
        return "Число должно быть меньше 10"
    elif a < 0 or c < 0:
        return "Числа должны быть положительными"
    elif c == 0:
            return "Делить на ноль нельзя"
    elif b == "+":
        return int(a + c)
    elif b == "-":
        return int(a - c)
    elif b == "/":
        return int(a // c)
    elif b == "*":
        return int(a * c)
    else:
        return "Ошибка ввода"
I = input()
result = main(I)
print("Результат:", result)
