#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve)
{
    int answer = n - lost.size();
    vector<int> check(n + 1, 1);
    for (int i = 0; i < lost.size(); ++i)
        check[lost[i]]--;
    for (int i = 0; i < reserve.size(); ++i)
    {
        if (check[reserve[i]] == 0)
        {
            check[reserve[i]] = 1;
            reserve[i] = -1;
            answer++;
        }
    }
    for (int i = 0; i < reserve.size(); ++i)
    {
        if (answer == n)
            break;
        if (reserve[i] == -1)
            continue;
        if (check[reserve[i] - 1] == 0 && reserve[i] > 1)
        {
            check[reserve[i] - 1] = 1;
            answer++;
            continue;
        }
        if (check[reserve[i] + 1] == 0 && reserve[i] != n)
        {
            check[reserve[i] + 1] = 1;
            answer++;
        }
    }
    return answer;
}