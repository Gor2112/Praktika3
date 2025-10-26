# Алгоритмы сортировки и поиска на Python

def bubble_sort(arr):
    """
    Реализация пузырьковой сортировки.
    Сложность: O(n²) в худшем случае, O(n) в лучшем случае
    """
    n = len(arr)
    
    # Проходим по всем элементам массива
    for i in range(n - 1):
        swapped = False
        
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем местами, если они в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Если на этом проходе не было обменов, массив уже отсортирован
        if not swapped:
            break

def shell_sort(arr):
    """
    Реализация сортировки Шелла.
    Сложность: зависит от выбора последовательности шагов
    """
    n = len(arr)
    gap = n // 2  # Начальный шаг - половина длины массива
    
    # Уменьшаем шаг до 1
    while gap > 0:
        
        # Применяем сортировку вставками для элементов на расстоянии шага
        for i in range(gap, n):
            temp = arr[i]  # Текущий элемент для вставки
            j = i
            
            # Сдвигаем элементы, которые больше временного
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Вставляем временный элемент на правильную позицию
            arr[j] = temp
        
        # Уменьшаем шаг вдвое
        gap //= 2

def partition(arr, low, high):
    """
    Вспомогательная функция для быстрой сортировки.
    Разделяет массив на две части относительно опорного элемента.
    """
    pivot = arr[high]  # Выбираем последний элемент как опорный
    i = low - 1  # Индекс меньшего элемента
    
    for j in range(low, high):
        # Если текущий элемент меньше или равен опоре
        if arr[j] <= pivot:
            i += 1
            # Меняем местами элементы
            arr[i], arr[j] = arr[j], arr[i]
    
    # Помещаем опорный элемент на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    """
    Реализация быстрой сортировки (Quick Sort).
    Сложность: O(n log n) в среднем случае, O(n²) в худшем случае
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Разделяем массив и получаем индекс опорного элемента
        pi = partition(arr, low, high)
        
        # Рекурсивно сортируем элементы до и после опорного
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def linear_search(arr, target):
    """
    Реализация линейного поиска.
    Сложность: O(n) в худшем случае, O(1) в лучшем случае
    """
    for index, element in enumerate(arr):
        if element == target:
            return index  # Возвращаем индекс найденного элемента
    return -1  # Элемент не найден

def fibonacci_search(arr, target):
    """
    Реализация поиска Фибоначчи.
    Сложность: O(log n)
    Работает только на отсортированных массивах
    """
    n = len(arr)
    
    # Инициализируем числа Фибоначчи
    fib_m2 = 0  # F(k-2)
    fib_m1 = 1  # F(k-1)
    fib_m = fib_m1 + fib_m2  # F(k)
    
    # Находим наименьшее число Фибоначчи, большее или равное размеру массива
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1  # Начальное смещение
    
    while fib_m > 1:
        # Проверяем элемент на позиции fibM2
        index = min(offset + fib_m2, n - 1)
        
        if arr[index] < target:
            # Сдвигаемся вправо
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = index
            
        elif arr[index] > target:
            # Сдвигаемся влево
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
            
        else:
            return index  # Элемент найден
    
    # Проверяем последний элемент
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1  # Элемент не найден

def demonstrate_algorithms():
    """Функция для демонстрации работы всех алгоритмов"""
    
    # Тестовые данные
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
    sorted_array = [11, 12, 22, 25, 34, 42, 50, 64, 76, 88, 90]
    
    print("Original array:", test_array)
    
    # Демонстрация пузырьковой сортировки
    array1 = test_array.copy()
    bubble_sort(array1)
    print("Bubble Sort:", array1)
    
    # Демонстрация сортировки Шелла
    array2 = test_array.copy()
    shell_sort(array2)
    print("Shell Sort:", array2)
    
    # Демонстрация быстрой сортировки
    array3 = test_array.copy()
    quick_sort(array3)
    print("Quick Sort:", array3)
    
    # Демонстрация линейного поиска
    target = 42
    result = linear_search(sorted_array, target)
    print(f"Linear Search for {target}: index {result}")
    
    # Демонстрация поиска Фибоначчи
    result = fibonacci_search(sorted_array, target)
    print(f"Fibonacci Search for {target}: index {result}")

# Примеры использования отдельных алгоритмов
if __name__ == "__main__":
    
    # Пример 1: Сортировка пузырьком
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Before bubble sort:", arr1)
    bubble_sort(arr1)
    print("After bubble sort:", arr1)
    print()
    
    # Пример 2: Сортировка Шелла
    arr2 = [23, 12, 1, 8, 34, 54, 2, 3]
    print("Before shell sort:", arr2)
    shell_sort(arr2)
    print("After shell sort:", arr2)
    print()
    
    # Пример 3: Быстрая сортировка
    arr3 = [10, 7, 8, 9, 1, 5]
    print("Before quick sort:", arr3)
    quick_sort(arr3)
    print("After quick sort:", arr3)
    print()
    
    # Пример 4: Линейный поиск
    arr4 = [2, 3, 4, 10, 40]
    target = 10
    result = linear_search(arr4, target)
    print(f"Linear search for {target} in {arr4}: index {result}")
    print()
    
    # Пример 5: Поиск Фибоначчи
    arr5 = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target = 85
    result = fibonacci_search(arr5, target)
    print(f"Fibonacci search for {target} in {arr5}: index {result}")
    print()
    
    # Демонстрация всех алгоритмов
    print("=== All Algorithms Demo ===")
    demonstrate_algorithms()
