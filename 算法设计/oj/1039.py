from collections import deque

def topological_sort(n, m, edges):
    # 初始化图的邻接表和入度数组
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    # 构建图和计算每个节点的入度
    for x, y in edges:
        adj[x].append(y)
        in_degree[y] += 1
    
    # 使用队列存放入度为 0 的节点
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # 减少相邻节点的入度
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 如果结果中节点的个数不等于n，说明存在环
    if len(result) != n:
        return "0"
    
    return " ".join(map(str, result))

def solve():
    t = int(input())  # 读取测试数据组数
    
    for _ in range(t):
        n, m = map(int, input().split())  # 读取 n 和 m
        edges = []
        
        for _ in range(m):
            x, y = map(int, input().split())
            edges.append((x, y))
        
        # 调用拓扑排序函数并输出结果
        result = topological_sort(n, m, edges)
        print(result)

# 调用 solve 函数
solve()
