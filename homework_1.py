# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def PowNumber(number1, number2):
    if number2 == 0:
        return 1
    return number1 * PowNumber(number1, number2 - 1)


number1, number2 = int(input("Введите число: ")), int(input("Введите необходимую степень: "))
print(f"Результат возведения в степень равно: {PowNumber(number1, number2)}")