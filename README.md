# Lab-11
Лабораторна робота 11: Робота з функціями у Python

Мета роботи:
Мета цієї лабораторної роботи полягає в тому, щоб навчитися працювати з функціями у мові програмування Python.

Опис завдання:
Завдання 1:
Написати функцію task1, яка приймає список чисел nums і повертає суму квадратів цих чисел.
Завдання 2:
Написати функцію task2, яка приймає список чисел nums і повертає суму чисел, які більші або рівні середньому значенню в цьому списку.
Завдання 3:
Написати функцію task3, яка приймає список чисел nums і повертає відсортований список за зменшенням частоти чисел, а у випадку однакової частоти - за зростанням самого числа.
Завдання 4:
Написати функцію task4, яка приймає список чисел nums, який складається з усіх чисел від 1 до n, окрім одного. Функція повертає це відсутнє число.
Завдання 5:
Написати функцію task5, яка приймає список цілих чисел nums і повертає довжину найбільшої послідовності чисел, що знаходяться поруч одне з одним.
Завдання 6:
Написати функцію task6, яка обертає список чисел nums на k позицій вправо.
Завдання 8:
Написати функцію task8, яка приймає список цілих чисел nums і повертає максимальну суму підпослідовності в цьому списку.
Завдання 10:
Написати функцію task10, яка приймає список координат точок points та ціле число k. Функція повертає перших k найближчих точок до початку координат, виміряних за евклідовою відстанню.

Виконання роботи:

Завдання 1:
def task1(nums):
    return sum(x ** 2 for x in nums)
    
Завдання 2:
def task2(nums):
    avg = sum(nums) / len(nums)
    return sum(x for x in nums if x >= avg)
    
Завдання 3:
def task3(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    return sorted(nums, key=lambda x: (-frequency[x], x))
    
Завдання 4:
def task4(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)
    
Завдання 5:
def task5(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length
    
Завдання 6:
def task6(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]
    
Завдання 8:
def task8(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
    
Завдання 10:
def task10(points, k):
    points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
    return points[:k]
    
Вимоги до середовища:Python 3.x
