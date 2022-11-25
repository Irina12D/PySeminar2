# Задача 4
'''
    Написать программу, которая состоит 4 из этапов:
        - создает список из рандомных четырехзначных чисел
        - принимает с консоли цифру и удаляет ее из всех элементов списка
        - цифры каждого элемента суммирует пока результат не станет однозначным числом
        - из финального списка убирает все дублирующиеся элементы
        - после каждого этапа выводить результат в консоль
    Пример:
        - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
        - 2 этап: Введите цифру: 3
        - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
        - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
        - 3 этап: [3, 1, 5, 5, 3, 5, 4]
        - 4 этап: [3, 1, 5, 4]
'''
print('Задача 4')
from random import randint
my_list = []
def stage1():
    # случайно выберу длину списка: от 5-ти до 20-ти чисел
    n = randint(5, 20)
    for i in range(n):
        my_list.append(randint(1000, 9999))
    print("Этап 1:", *my_list)

# функция для удаления цифры из числа - реализация через строку
def del_digit(num, digit):
    # буду через строку удалять - для эффективной реализации
    # использую функцию замены (можно посимвольно пройтись и без функции обойтись, но я не буду себя ограничивать :))
    num = str(num)
    digit = str(digit)
    if digit in num:
        num = num.replace(digit, '')
    return int(num)

# функция для удаления цифры из числа - реализация через число
def del_digit_from_number(num, digit):
    # если подразумевалась обработка числа, то приведу вариант удаления из числа
    s = 0
    st = 1
    while num != 0:
        c = num % 10
        if c != digit:
            s += c * st
            st *= 10
        num //= 10
    return s

def stage2():
    c = int(input("Этап 2:Введите цифру: "))
    n = len(my_list)
    for i in range(n):
        my_list[i] = del_digit(my_list[i], c)
    print("Этап 2:", *my_list)

# функция для суммирования цифр числа
def num_to_digit(num):
    # реализация через строку, чтоб не использовать операции деления
    num = str(num)
    while len(num) != 1:
        list_symbols = [int(i) for i in num]
        num = str(sum(list_symbols))
    return int(num)

def stage3():
    n = len(my_list)
    for i in range(n):
        my_list[i] = num_to_digit(my_list[i])
    print("Этап 3:", *my_list)

def stage4():
    result = [my_list[0]]
    for i in my_list:
        if not(i in result):
            result.append(i)
    print("Этап 4:", *result)

stage1()
stage2()
stage3()
stage4()