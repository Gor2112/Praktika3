import math

def tsp_2_approximation(dist_matrix):
    n = len(dist_matrix)
    
    # 1. Построение MST (алгоритм Прима)
    def prim_mst():
        visited = [False] * n
        min_edge = [math.inf] * n
        parent = [-1] * n
        min_edge[0] = 0
        
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_edge[i] < min_edge[u]):
                    u = i
            visited[u] = True
            
            for v in range(n):
                if not visited[v] and dist_matrix[u][v] < min_edge[v]:
                    min_edge[v] = dist_matrix[u][v]
                    parent[v] = u
        return parent
    
    # 2. Построение и удвоение MST
    parent = prim_mst()
    mst_adj = [[] for _ in range(n)]
    for i in range(1, n):
        mst_adj[i].append(parent[i])
        mst_adj[parent[i]].append(i)
    
    # 3. Поиск эйлерова цикла
    def euler_tour(start):
        stack = [start]
        euler_path = []
        visited_edges = set()
        
        while stack:
            u = stack[-1]
            found = False
            for v in mst_adj[u]:
                edge = tuple(sorted((u, v)))
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    stack.append(v)
                    found = True
                    break
            if not found:
                euler_path.append(stack.pop())
        return euler_path
    
    # 4. Построение гамильтонова цикла
    euler_path = euler_tour(0)
    visited = [False] * n
    hamiltonian_cycle = []
    
    for vertex in euler_path:
        if not visited[vertex]:
            visited[vertex] = True
            hamiltonian_cycle.append(vertex)
    hamiltonian_cycle.append(hamiltonian_cycle[0])
    
    # 5. Расчет стоимостей
    approx_cost = sum(dist_matrix[hamiltonian_cycle[i]][hamiltonian_cycle[i+1]] 
                     for i in range(len(hamiltonian_cycle)-1))
    mst_cost = sum(dist_matrix[i][parent[i]] for i in range(1, n))
    ratio = approx_cost / mst_cost
    
    return hamiltonian_cycle, approx_cost, mst_cost, ratio

# Пример использования
dist_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 40],
    [20, 25, 30, 0, 45],
    [25, 30, 40, 45, 0]
]

route, approx_cost, mst_cost, ratio = tsp_2_approximation(dist_matrix)

print("Маршрут:", route)
print("Стоимость:", approx_cost)
print("Нижняя оценка (MST):", mst_cost)
print("Соотношение:", f"{ratio:.3f}")
