def dfs(graph, start):
    """
    Простой DFS с временем входа и выхода
    graph: список смежности графа
    start: начальная вершина
    """
    n = len(graph)
    visited = [False] * n      # Посещенные вершины
    entry_time = [-1] * n      # Время входа
    exit_time = [-1] * n       # Время выхода
    time = 0                   # Счетчик времени
    
    def dfs_recursive(vertex):
        nonlocal time  # Используем внешнюю переменную time
        
        # Вход в вершину
        visited[vertex] = True
        entry_time[vertex] = time
        time += 1
        print(f"Вход в {vertex} (время: {entry_time[vertex]})")
        
        # Посещаем всех соседей
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs_recursive(neighbor)
        
        # Выход из вершины
        exit_time[vertex] = time
        time += 1
        print(f"Выход из {vertex} (время: {exit_time[vertex]})")
    
    # Запускаем DFS
    dfs_recursive(start)
    
    # Выводим результаты
    print("\nРезультаты:")
    for i in range(n):
        print(f"Вершина {i}: вход={entry_time[i]}, выход={exit_time[i]}")
    
    return entry_time, exit_time

# Пример:
if __name__ == "__main__":
    # Граф в виде списка смежности
    # graph[i] содержит список соседей вершины i
    graph = [
        [1, 2],     # Вершина 0 -> 1, 2
        [3],        # Вершина 1 -> 3
        [4],        # Вершина 2 -> 4
        [5],        # Вершина 3 -> 5
        [5],        # Вершина 4 -> 5
        []          # Вершина 5 -> нет соседей
    ]
    
    # Запускаем DFS из вершины 0
    entry, exit = dfs(graph, 0)