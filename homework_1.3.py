'''Септиянто Андре - 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

'''
n = input('input_number:')
a = int(str(n)+str(n))
b = int(str(n)+str(n)+str(n))
c = int(int(n)+int(a)+int(b))
str = (f' Считаем {n} + {a} + {b} = {c}')
print(str)