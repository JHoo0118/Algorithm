#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {

    int answer = 1000;
    if (s.length() == 1) answer = 1;

    for (int c = 1 ; c < s.length() / 2 + 1; ++c) {

        int t = -1, cnt = 1;
        string result, prev, tmp;

        while (++t < c) prev += s[t];

        for (int i = c; i < s.length(); i += c) {

            t = i - 1;

            while (++t < i + c) {
                if (t >= s.length()) break;
                tmp += s[t];
            }

            if (prev.compare(tmp) == 0) cnt += 1;
            else {
                result += cnt >= 2 ? to_string(cnt) + prev : prev;
                prev = tmp;
                cnt = 1;
            }

            tmp.clear();

        }

        result += cnt >= 2 ? to_string(cnt) + prev : prev;
        answer = answer < result.length() ? answer : result.length();
    }
    return answer;
}