#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

int main(void)
{
    std::vector<std::pair<int, int>> AB;
    int N, M;
    std::cin >> N >> M;

    int a, b;
    for (int i = 0; i < M; ++i)
    {
        std::cin >> a >> b;
        AB.push_back(std::make_pair(a, b));
    }

    std::sort(AB.begin(), AB.end());
    int min_b = AB[0].second;
    int cnt = 1;
    for (int i = 0; i < M; ++i)
    {
        if (min_b <= AB[i].first)
        {
            ++cnt;
            min_b = AB[i].second;
        }
        else
        {
            min_b = std::min(min_b, AB[i].second);
        }
    }

    std::cout << cnt << std::endl;
    return 0;
}
