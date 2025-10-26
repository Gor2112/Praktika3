#include <iostream>
#include <vector>
#include <algorithm>

// 1. Сортировка выбором (Selection Sort)
void selectionSort(std::vector<int>& data) {
    size_t size = data.size();
    for (size_t current = 0; current < size - 1; ++current) {
        size_t minPosition = current; // Предполагаем, что текущий элемент минимальный
        
        // Ищем минимальный элемент в оставшейся части массива
        for (size_t next = current + 1; next < size; ++next) {
            if (data[next] < data[minPosition]) {
                minPosition = next; // Нашли новый минимальный элемент
            }
        }
        
        // Если нашли элемент меньше текущего, меняем их местами
        if (minPosition != current) {
            std::swap(data[current], data[minPosition]);
        }
    }
}

// 2. Сортировка вставками (Insertion Sort)
void insertionSort(std::vector<int>& data) {
    size_t size = data.size();
    
    // Начинаем со второго элемента (индекс 1)
    for (size_t i = 1; i < size; ++i) {
        int currentValue = data[i]; // Текущий элемент для вставки
        int position = i - 1; // Начинаем сравнение с предыдущего элемента
        
        // Сдвигаем элементы большие currentValue вправо
        while (position >= 0 && data[position] > currentValue) {
            data[position + 1] = data[position];
            --position;
        }
        
        // Вставляем currentValue на правильную позицию
        data[position + 1] = currentValue;
    }
}

// 3. Сортировка слиянием (Merge Sort)
// Вспомогательная функция для слияния двух отсортированных массивов
void mergeArrays(std::vector<int>& data, int start, int middle, int end) {
    // Размеры левой и правой частей
    int leftSize = middle - start + 1;
    int rightSize = end - middle;
    
    // Создаем временные массивы для левой и правой частей
    std::vector<int> leftPart(leftSize);
    std::vector<int> rightPart(rightSize);
    
    // Копируем данные во временные массивы
    for (int i = 0; i < leftSize; ++i)
        leftPart[i] = data[start + i];
    for (int j = 0; j < rightSize; ++j)
        rightPart[j] = data[middle + 1 + j];
    
    // Индексы для левой, правой частей и основного массива
    int i = 0, j = 0, k = start;
    
    // Сливаем временные массивы обратно в основной массив
    while (i < leftSize && j < rightSize) {
        if (leftPart[i] <= rightPart[j]) {
            data[k] = leftPart[i];
            ++i;
        } else {
            data[k] = rightPart[j];
            ++j;
        }
        ++k;
    }
    
    // Копируем оставшиеся элементы левой части (если есть)
    while (i < leftSize) {
        data[k] = leftPart[i];
        ++i;
        ++k;
    }
    
    // Копируем оставшиеся элементы правой части (если есть)
    while (j < rightSize) {
        data[k] = rightPart[j];
        ++j;
        ++k;
    }
}

// Основная рекурсивная функция сортировки слиянием
void mergeSort(std::vector<int>& data, int start, int end) {
    // Базовый случай рекурсии - массив из одного элемента уже отсортирован
    if (start >= end) return;
    
    // Находим середину массива
    int middle = start + (end - start) / 2;
    
    // Рекурсивно сортируем левую и правую части
    mergeSort(data, start, middle);
    mergeSort(data, middle + 1, end);
    
    // Сливаем отсортированные части
    mergeArrays(data, start, middle, end);
}

// Обертка для удобного вызова сортировки слиянием
void mergeSort(std::vector<int>& data) {
    if (data.empty()) return;
    mergeSort(data, 0, data.size() - 1);
}

// 4. Пирамидальная сортировка (Heap Sort)
// Функция для преобразования поддерева в кучу (heapify)
void heapify(std::vector<int>& data, int heapSize, int rootIndex) {
    int largestIndex = rootIndex; // Инициализируем наибольший элемент как корень
    int leftChild = 2 * rootIndex + 1; // Левый потомок
    int rightChild = 2 * rootIndex + 2; // Правый потомок
    
    // Если левый потомок больше корня
    if (leftChild < heapSize && data[leftChild] > data[largestIndex])
        largestIndex = leftChild;
    
    // Если правый потомок больше текущего наибольшего
    if (rightChild < heapSize && data[rightChild] > data[largestIndex])
        largestIndex = rightChild;
    
    // Если наибольший элемент не корень
    if (largestIndex != rootIndex) {
        std::swap(data[rootIndex], data[largestIndex]);
        
        // Рекурсивно преобразуем в кучу затронутое поддерево
        heapify(data, heapSize, largestIndex);
    }
}

// Основная функция пирамидальной сортировки
void heapSort(std::vector<int>& data) {
    int size = data.size();
    
    // Построение кучи (перегруппируем массив)
    for (int i = size / 2 - 1; i >= 0; --i)
        heapify(data, size, i);
    
    // Один за другим извлекаем элементы из кучи
    for (int i = size - 1; i > 0; --i) {
        // Перемещаем текущий корень в конец
        std::swap(data[0], data[i]);
        
        // Вызываем heapify на уменьшенной куче
        heapify(data, i, 0);
    }
}

// 5. Бинарный поиск (Binary Search)
int binarySearch(const std::vector<int>& data, int target) {
    int left = 0; // Левая граница поиска
    int right = data.size() - 1; // Правая граница поиска
    
    while (left <= right) {
        // Находим средний элемент
        int middle = left + (right - left) / 2;
        
        // Если нашли целевой элемент
        if (data[middle] == target)
            return middle;
        
        // Если целевой элемент меньше среднего, ищем в левой половине
        if (data[middle] < target)
            left = middle + 1;
        // Если целевой элемент больше среднего, ищем в правой половине
        else
            right = middle - 1;
    }
    
    // Элемент не найден
    return -1;
}

// 6. Интерполяционный поиск (Interpolation Search)
int interpolationSearch(const std::vector<int>& data, int target) {
    int low = 0; // Нижняя граница
    int high = data.size() - 1; // Верхняя граница
    
    while (low <= high && target >= data[low] && target <= data[high]) {
        // Особый случай: когда границы совпадают
        if (low == high) {
            if (data[low] == target) return low;
            return -1;
        }
        
        // Вычисляем позицию с помощью интерполяционной формулы
        int estimate = low + (((double)(high - low) / 
                          (data[high] - data[low])) * (target - data[low]));
        
        // Если нашли целевой элемент
        if (data[estimate] == target)
            return estimate;
            
        // Если целевой элемент меньше предполагаемого, ищем в левой части
        if (data[estimate] < target)
            low = estimate + 1;
        // Если целевой элемент больше предполагаемого, ищем в правой части
        else
            high = estimate - 1;
    }
    
    // Элемент не найден
    return -1;
}

// Функция для демонстрации работы всех алгоритмов
void demonstrateAlgorithms() {
    std::vector<int> testData = {64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42};
    std::vector<int> sortedData = {11, 12, 22, 25, 34, 42, 50, 64, 76, 88, 90};
    
    std::cout << "Исходные данные: ";
    for (int num : testData) std::cout << num << " ";
    std::cout << std::endl;
    
    // Тестируем сортировку выбором
    std::vector<int> data1 = testData;
    selectionSort(data1);
    std::cout << "Сортировка выбором: ";
    for (int num : data1) std::cout << num << " ";
    std::cout << std::endl;
    
    // Тестируем сортировку вставками
    std::vector<int> data2 = testData;
    insertionSort(data2);
    std::cout << "Сортировка вставками: ";
    for (int num : data2) std::cout << num << " ";
    std::cout << std::endl;
    
    // Тестируем сортировку слиянием
    std::vector<int> data3 = testData;
    mergeSort(data3);
    std::cout << "Сортировка слиянием: ";
    for (int num : data3) std::cout << num << " ";
    std::cout << std::endl;
    
    // Тестируем пирамидальную сортировку
    std::vector<int> data4 = testData;
    heapSort(data4);
    std::cout << "Пирамидальная сортировка: ";
    for (int num : data4) std::cout << num << " ";
    std::cout << std::endl;
    
    // Тестируем бинарный поиск
    int target = 42;
    int result = binarySearch(sortedData, target);
    std::cout << "Бинарный поиск числа " << target << ": индекс " << result << std::endl;
    
    // Тестируем интерполяционный поиск
    result = interpolationSearch(sortedData, target);
    std::cout << "Интерполяционный поиск числа " << target << ": индекс " << result << std::endl;
}

int main() {
    demonstrateAlgorithms();
    return 0;
}
