#include <iostream>
#include <vector>

int main(void)
{
    int N;
    std::cin >> N;

    std::vector<int> A;
    int ai;
    for (int i = 0; i < N; ++i)
    {
        std::cin >> ai;
        A.push_back(ai);
    }

    int cnt = 0;
    for (int i = 0; i < N - 1; ++i)
    {
        if (A[i] == A[i+1])
        {
            ++cnt;
            ++i;
        }
    }

    std::cout << cnt << std::endl;
    return 0;
}
