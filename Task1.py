# Задача 1
'''
    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
    Пример:
    6782 -> 23
    0,56 -> 11
'''

'''
    Самый эффективный способ - это обработать число в виде строки. 
    Если обрабатывать число в виде числа, то придётся выделять цифры.
    Для выделения цифр числа используются операции деления (делить нацело на 10, остаток от деления на 10).
    Операции деления - самые трудоёмкие из арифметических операций (на машинном уровне),
    поэтому для эффективной реализации задачи на любом языке программирования лучше представить число строкой
    и обработать посимвольно.

    P.S. В примере на занятии, когда разбирали ввод данных для задачи,
         где нужен был ввод точек на плоскости или в пространстве...
         Ты вводил списком и проверял длину списка, чтобы узнать размерность вводимых данных.
         Там была операция: if len(my_list) / 2 == 2 - это 2D, а если == 3, то 3D.
         Так вот, тут тоже бы лучше было длину сравнивать с 4 и 6 (то есть не использовать деление),
         либо (если где, например, нужно было бы делить на какое-то значение n): if len(my_list) == 2*n (или 3*n)
         То есть первое правило использования операции деления - не использовать операцию деления, если это возможно

         Это, конечно, уже тонкости программирования, просто решила описать, раз уж про эффективный способ тут написала

         И ещё один Пы.Сы. (понесло меня что-то :))) decimal - это представление вещественных чисел с фиксированной точкой.
         double, float - это с плавающей, а decimal - с фиксированной, поэтому где важна точность (например, при работе
         с финансовыми данными), используют decimal. Этот тип есть и в С# 

         Ну всё, теперь решение...        
'''
print('Задача 1')
n = input('Введите вещественное число ')
summa = 0
for i in n:
    if i.isdigit():  # проверяем, что символ цифра. Можно i != '.'
        summa += int(i)
print(summa)