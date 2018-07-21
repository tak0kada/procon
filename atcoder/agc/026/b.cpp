#include <iostream>
#include <algorithm>

int main(void)
{
    int t;
    std::cin >> t;
    long a, b, c, d;
    for (int i = 0; i < t; ++i)
    {
        std::cin >> a >> b >> c >> d;
        std::cout << a << b << c << d;
        if (b > a || d < b)
        {
            std::cout << "no" << std::endl;
            continue;
        }
        if (c >= b && d >= b) // d >= b is always true
        {
            std::cout << "yes" << std::endl;
            continue;
        }

        // a <= b, c < b, d > b
        int A = a % b, B = a % b, C = c % b, D = d % b;
        if (A > C)
        {
            std::cout << "no" << std::endl;
        }
        else
        {
            // true if B and D are coprime
            // false if B and D are not coprime
            while (B > 0 || D > 0)
            {
                B = std::min(B, D);
                D = std::max(B, D) % std::min(B, D);
            }
            if (B == 0 || D == 1)
                std::cout << "yes" << std::endl;
            else if (B == 0 && D == 0)
                std::cout << "no" << std::endl;
        }
    }

    return 0;
}
