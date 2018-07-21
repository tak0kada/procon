#include <iostream>
#include <vector>
#include <numeric>

int main(void)
{
    int N;
    std::cin >> N;

    std::vector<int> A;
    int tmp;
    for (int i = 0; i < N; ++i)
    {
        std::cin >> tmp;
        A.push_back(tmp);
    }
    std::cout << std::accumulate(A.begin(), A.end(), 0) - N << std::endl;
    return 0;
}
