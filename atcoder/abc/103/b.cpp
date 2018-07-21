#include <iostream>
#include <string>

bool compare(const std::string& lhs, const std::string& rhs)
{
    if (lhs.size() != rhs.size())
        return false;
    if (lhs == rhs)
        return true;

    std::size_t l = lhs.size();
    for (auto i = 1; i < l; ++i)
    {
        if (lhs.substr(l-i, i) == rhs.substr(0, i) && lhs.substr(0, l-i) == rhs.substr(i, l-i))
            return true;
    }
    return false;
}

int main(void)
{
    std::string lhs, rhs;
    std::getline(std::cin, lhs);
    std::getline(std::cin, rhs);
    std::cout << (compare(lhs, rhs)? "Yes": "No") << std::endl;
    return 0;
}
