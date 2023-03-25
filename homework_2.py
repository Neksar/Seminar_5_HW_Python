# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def SumNumbers(number1, number2):
    number1 += 1
    number2 -= 1
    if number2 > 0:
        return SumNumbers(number1, number2)
    return number1

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(f"Результат сложения числа {number1} и числа {number2} равен: {SumNumbers(number1, number2)}")

