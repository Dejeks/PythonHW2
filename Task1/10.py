"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть. 
С клавиатуры вводятся МОНЕТЫ построчно.
"""

arr = list(map(int,input().split()))
count = 0

for i in range(len(arr)):
    if arr[i] == 1:
        count += 1

print(count if count < len(arr)/2 else len(arr) - count)
