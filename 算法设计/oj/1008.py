import bisect

def solve():
    M = int(input())  # 读取测试数据组数
    for _ in range(M):
        missiles = list(map(int, input().split()))[1:]  # 读取每组数据中的导弹高度
        
        # 解决问题 1: 找到最大能拦截的导弹数量 (最长递减子序列)
        n = len(missiles)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if missiles[i] <= missiles[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_intercept = max(dp)  # 最大能拦截的导弹数量

        # 解决问题 2: 最少需要多少套拦截系统 (贪心算法)
        intercept_systems = []
        
        for missile in missiles:
            # 尝试将当前导弹放入已有的拦截系统中
            pos = bisect.bisect_right(intercept_systems, missile)
            if pos < len(intercept_systems):
                intercept_systems[pos] = missile  # 放入现有系统
            else:
                intercept_systems.append(missile)  # 新开一个系统
        
        min_systems = len(intercept_systems)  # 最少需要的系统数
        
        print(f"{max_intercept} {min_systems}")

# 调用solve函数
solve()
