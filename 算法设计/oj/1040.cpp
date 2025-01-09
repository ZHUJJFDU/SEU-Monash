#include <iostream>
#include <vector>

using namespace std;

// 搜索二维矩阵的函数
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }

    int m = matrix.size();        // 行数
    int n = matrix[0].size();     // 列数
    int row = 0;                  // 从第0行开始
    int col = n - 1;             // 从最后一列开始

    // 遍历矩阵，直到找到目标或者超出边界
    while (row < m && col >= 0) {
        if (matrix[row][col] == target) {
            return true;         // 找到目标，返回true
        } else if (matrix[row][col] > target) {
            col--;              // 当前元素大于目标，向左移动
        } else {
            row++;              // 当前元素小于目标，向下移动
        }
    }

    return false;                // 如果没有找到目标，返回false
}

int main() {
    int nums;                     // 测试用例数
    cin >> nums;

    while (nums--) {
        int m, n, target;         // m行 n列 目标值
        cin >> m >> n >> target;

        vector<vector<int>> matrix(m, vector<int>(n));
        
        // 读取矩阵
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> matrix[i][j];
            }
        }

        // 调用搜索函数并输出结果
        if (searchMatrix(matrix, target)) {
            cout << "true" << endl;
        } else {
            cout << "false" << endl;
        }
    }

    return 0;
}
