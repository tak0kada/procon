#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

/*
template <class T>
std::ostream& operator<< (std::ostream& stream, const std::vector<T>& vec)
{
    stream << "[ ";
    for (const auto &i: vec) stream << i << " ";
    stream << "]";
    return stream;
}
*/

int solve()
{
    using namespace std;
    
    // input
    int n_input;
    cin >> n_input;
    vector<int> d(n_input);
    for (int i = 0; i < n_input; ++i)
    {
        cin >> d[i];
    }
    int goal_x, goal_y;
    cin >> goal_x >> goal_y;
    int goal = max(abs(goal_x), abs(goal_y));
    
    // algorithm
    if (goal == 0)
        return 0;
    else
    {
        int max_d = *max_element(d.begin(), d.end());
        if (goal >= max_d)
            return (goal / max_d) + (goal % max_d == 0 ? 0 : 1);
        else
        {
            for (const auto& i: d)
            {
                if (i == goal)
                    return 1;
            }
            return 2;
        }
    }
}

int main(void)
{
    std::cout << solve() << std::endl;
    return 0;
}
