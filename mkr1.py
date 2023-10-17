import random

def random_array(n):
    array = [] #Створення масиву
    for i in range(n):
        row = [] #Створення рядка
        for j in range(n):
            row.append(random.randint(1, 99))  #Заповнення масиву рандомними числами
        array.append(row) #Додаємо рядок до масиву
    return array

def average_row(row):
    if len(row) == 0:           #Визначення середнього значення у кожному рядку масиву
        return 0
    return sum(row) / len(row)

def sort_array(array): #Сортування масиву в залежності від середнього значення
    n = len(array)

    for i in range(n):
        key_row = array[i] 
        key_avg = average_row(key_row) 
        j = i - 1

        while j >= 0 and average_row(array[j]) > key_avg: 
            array[j + 1] = array[j] #Сортування
            j -= 1
        array[j + 1] = key_row

    return array

n = int(input("Введіть розмірність масиву: "))

array = random_array(n)
print("Початковий масив:")
for row in array:
    for num in row:
        print(f"{num:<4}", end=' ') #Вивід елементів рядка
    print()

sorted_array = sort_array(array)
print("Відсортований масив:")
for row in sorted_array:
    for num in row:
        print(f"{num:<4}", end=' ') #Вивід відсортованого масиву
        avg = average_row(row)
    print(f"Середнє: {avg:<6.2f}")
