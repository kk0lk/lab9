"""
Задача №1 

Напишіть програму, яка реалізує класичний алгоритм сортування стовпців двовимірного масиву методом підрахунку. 
Розмірність масиву та всі елементи генеруються за допомогою випадкових чисел.

Виконала студентка 31І групи Гриб Наталія
"""




import random

def generate_random_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    total = 0
    for i in range(max_val + 1):
        count[i], total = total, count[i] + total

    for num in arr:
        output[count[num]] = num
        count[num] += 1

    return output

def sort_columns_by_counting(matrix):
    rows = len(matrix)
    if rows == 0:
        return matrix

    cols = len(matrix[0])
    max_val = max(max(row) for row in matrix)

    sorted_matrix = [[0] * cols for _ in range(rows)]
    for col in range(cols):
        column = [matrix[row][col] for row in range(rows)]
        sorted_column = counting_sort(column, max_val)
        for row in range(rows):
            sorted_matrix[row][col] = sorted_column[row]

    return sorted_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Параметри для генерації випадкового масиву
rows = 5
cols = 4
min_val = 0
max_val = 9

# Генерація випадкового масиву
matrix = generate_random_matrix(rows, cols, min_val, max_val)
print("Оригінальний масив:")
print_matrix(matrix)

# Сортування стовпців методом підрахунку
sorted_matrix = sort_columns_by_counting(matrix)
print("\nВідсортований масив:")
print_matrix(sorted_matrix)
