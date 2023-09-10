def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # Левый потомок
    r = 2 * i + 2  # Правый потомок

    # Если левый дочерний элемент больше родителя
    if l < n and arr[i] < arr[l]:
        largest = l

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Если самый большой элемент не является корневым, то меняем их местами
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Рекурсивно вызываем функцию heapify для поддерева
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Построение max-кучи (переупорядочивание массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи один за другим
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем корень и последний элемент
        heapify(arr, i, 0)

    return arr


# Пример использования программы
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Отсортированный массив:", sorted_arr)
