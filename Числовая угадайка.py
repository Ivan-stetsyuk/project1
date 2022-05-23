import random

s = random.randint(1, 100)
count = 0
print('Добро пожаловать в числовую угадайку')

def is_valid(n):
    if 1 <= n <= 100:
        return True
    else:
        return False

while True:
    print('Введите число от 1 до 100')
    n = int(input())
    is_valid(n)
    if is_valid(n) == True:
        break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

while n != s:
    if n < s:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif n > s:
        print('Ваше число больше загаданного, попробуйте еще разок')
    count += 1
    n = int(input())
print('Вы угадали c', count, 'попытки, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


