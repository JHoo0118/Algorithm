#include <iostream>
using namespace std;
const int inf = 1e9;
int n, m;
int graph[1001][1001];

int main()
{
    cin >> n >> m;
    for (int i = 0; i < 100; ++i)
        fill(graph[i], graph[i] + 100, inf);

    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            if (i == j)
                graph[i][j] = 0;

    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    for (int k = 1; k <= n; ++k)
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
            {
                if (graph[k][j] == inf)
                    continue;
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }

    int ans = 0, minv = inf, result = 0;
    for (int i = 1; i <= n; ++i)
    {
        result = 0;
        for (int j = 1; j <= n; ++j)
        {
            result += graph[i][j];
        }
        if (minv > result)
        {
            minv = result;
            ans = i;
        }
    }
    cout << ans << '\n';
    return 0;
}