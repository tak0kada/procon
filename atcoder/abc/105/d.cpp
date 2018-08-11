#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main(void)
{
    int N, M;
    std::vector<int> A;
    std::cin >> N >> M;
    for (int i = 0; i < N; ++i)
    {
        int a;
        std::cin >> a;
        A.push_back(a % M);
    }

    std::partial_sum(A.begin(), A.end(), A.begin(), [M](int a, int b){return (a+b) % M;});
    std::sort(A.begin(), A.end());

    std::vector<int> set;
    int n = 0, cnt = 1;
    for (auto a: A)
    {
        if (a != n)
        {
            set.push_back(cnt);
            n = a;
            cnt = 1;
        }
        else
        {
            cnt += 1;
        }
    }
    set.push_back(cnt);

    long ans = 0;
    for (auto s: set)
    {
        ans += static_cast<long>(s) * static_cast<long>(s - 1) / 2;
    }

    std::cout << ans << std::endl;
    return 0;
}
