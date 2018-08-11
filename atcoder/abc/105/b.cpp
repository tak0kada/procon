#include <iostream>

int main(void)
{
    int N;
    std::cin >> N;

    switch(N % 28)
    {
        case 0:
        case 4:
        case 7:
        case 8:
        case 11:
        case 12:
        case 14:
        case 15:
        case 16:
        case 18:
        case 19:
        case 20:
        case 21:
        case 22:
        case 23:
        case 24:
        case 25:
        case 26:
        case 27:
            std::cout << "Yes" << std::endl;
            break;
        default:
            std::cout << "No" << std::endl;
            break;
    }

    return 0;
}
