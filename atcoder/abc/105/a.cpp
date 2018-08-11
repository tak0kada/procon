#include <iostream>

int main(void)
{
    int N, K;
    std::cin >> N >> K;
    std::cout << (N%K == 0? 0: 1) << std::endl;
    return 0;
}
