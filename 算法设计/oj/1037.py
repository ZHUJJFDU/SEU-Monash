def dfs(u, match, visited, graph):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match[v] == -1 or dfs(match[v], match, visited, graph):
                match[v] = u
                return True
    return False

def max_match(n, m, graph):
    # `match[v]` represents the male guest matched to female v, -1 means unmatched
    match = [-1] * (m + 1)
    result = 0
    
    for u in range(1, n + 1):
        visited = [False] * (m + 1)
        if dfs(u, match, visited, graph):
            result += 1
            
    return result

def solve():
    T = int(input())  # Read number of test cases
    
    for _ in range(T):
        n, m = map(int, input().split())  # Read n and m
        
        graph = [[] for _ in range(n + 1)]  # Adjacency list for male to female
        
        for i in range(1, n + 1):
            data = list(map(int, input().split()))
            k = data[0]
            for j in data[1:]:
                graph[i].append(j)
        
        # Get the maximum match
        result = max_match(n, m, graph)
        print(result)

# Calling solve function
solve()
