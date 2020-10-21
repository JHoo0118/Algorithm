// https://www.acmicpc.net/problem/1010

#include <iostream>
using namespace std;
int r, n, t;
int cache[31][31];

int bino(int n, int r)
{
    if (r == 0 || r == n)
        return 1;
    if (cache[n][r] != -1)
        return cache[n][r];
    return cache[n][r] = bino(n - 1, r - 1) + bino(n - 1, r);
}

int main()
{
    cin >> t;
    while (t--)
    {
        fill(&cache[0][0], &cache[30][0], -1);
        cin >> r >> n;
        cout << bino(n, r) << '\n';
    }
    return 0;
}