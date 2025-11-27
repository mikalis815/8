def generate_permutations_recursive(s):
    """
    Генерирует все перестановки строки с помощью рекурсии.
    Аргументы:
        s (str): Входная строка
    Возвращает:
        Список всех перестановок строки
    """
    # Если строка пустая или содержит один символ
    if len(s) <= 1:
        return [s]
    
    permutations = []
    
    # Проходим по каждому символу в строке
    for i in range(len(s)):
        # Выбираем текущий символ как первый
        current_char = s[i]
        
        # Оставшаяся строка без текущего символа
        remaining_chars = s[:i] + s[i+1:]
        
        # Рекурсивно генерируем перестановки для оставшейся строки
        for perm in generate_permutations_recursive(remaining_chars):
            # Добавляем текущий символ в начало каждой перестановки
            permutations.append(current_char + perm)
    
    return permutations

# Пример: Все перестановки строки
input_string = "abc"
result = generate_permutations_recursive(input_string)
print(input_string)
for perm in result:
    print(perm)
#Количество перестановок
print(len(result))