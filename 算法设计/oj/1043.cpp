#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int superEggDrop(int K, int N) {
    // dp[k][n] 表示 k 个鸡蛋，n 层楼的最小投掷次数
    vector<vector<int>> dp(K + 1, vector<int>(N + 1, 0));

    // 初始化 dp
    for (int k = 1; k <= K; ++k) {
        dp[k][0] = 0;  // 0 层楼，0 次投掷
        dp[k][1] = 1;  // 1 层楼，1 次投掷
    }
    
    // 当只有一个鸡蛋时，需要逐层试探
    for (int n = 0; n <= N; ++n) {
        dp[1][n] = n;  // 只有一个鸡蛋时，需要 n 次投掷
    }

    // 填充 dp 数组
    for (int k = 2; k <= K; ++k) {
        for (int n = 2; n <= N; ++n) {
            int left = 1, right = n, res = INT_MAX;
            // 使用二分查找来优化
            while (left <= right) {
                int mid = left + (right - left) / 2;
                int breakEgg = dp[k - 1][mid - 1];  // 鸡蛋破了
                int noBreakEgg = dp[k][n - mid];   // 鸡蛋没有破
                int worst = max(breakEgg, noBreakEgg);
                res = min(res, 1 + worst);  // 1 是当前投掷的一次
                if (breakEgg > noBreakEgg) {
                    right = mid - 1;  // 如果破蛋的情况比较坏，减少楼层
                } else {
                    left = mid + 1;  // 如果不破蛋的情况比较坏，增加楼层
                }
            }
            dp[k][n] = res;
        }
    }

    return dp[K][N];
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int K, N;
        cin >> K >> N;
        cout << superEggDrop(K, N) << endl;
    }
    return 0;
}
