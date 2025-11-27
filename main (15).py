def find_max(arr):
    # Если в массиве один элемент, он и есть максимальный
    if len(arr) == 1:
        return arr[0]
    
    # Рекурсивный случай: сравниваем первый элемент с максимумом из остальных
    first = arr[0]
    max_rest = find_max(arr[1:])
    
    # Возвращаем большее значение
    if first > max_rest:
        return first
    else:
        return max_rest

# Пример:
numbers = [3, 7, 2, 9, 1]
result = find_max(numbers)
print(result)