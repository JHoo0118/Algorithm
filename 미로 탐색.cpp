# https://www.acmicpc.net/problem/2178
#include <iostream>
#include <queue>
using namespace std;

int n, m;
int a[100][100];
int s[100][100];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push({x, y});
    s[x][y] = 1;
    while (!q.empty()) {
        x = q.front().first, y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (a[nx][ny] == 1 && s[nx][ny] == 0) {
                q.push({nx, ny});
                s[nx][ny] += s[x][y] + 1;
            }
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            scanf("%1d", &a[i][j]);
        }
    }
    bfs(0, 0);
    cout << s[n - 1][m - 1] << '\n';
    return 0;
}