#include <iostream>

int main(void)
{

    int tmp;
    std::cin >> tmp;
    int min = tmp, max = tmp;
    for (int i = 1; i < 3; ++i)
    {
        std::cin >> tmp;
        if (tmp < min)
            min = tmp;
        if (tmp > max)
            max = tmp;
    }

    std::cout << max - min << std::endl;
    return 0;
}
