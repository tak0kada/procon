#include <iostream>
#include <string>

int main(void)
{
    int N;
    std::cin >> N;
    std::string ans;

    if (N == 0)
        ans = "0";

    while (N != 0)
    {
        ans = std::to_string(N % 2 != 0) + ans;
        if (N > 0)
        {
            N = - (N - N%2) / 2;
        }
        else
        {
            N = - (N + N%2) / 2;
        }
    }

    std::cout << ans << std::endl;
    return 0;
}
