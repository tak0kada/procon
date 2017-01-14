#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int solve(string input)
{
    int pos_first = input.find("ccw");
    int pos_last = input.rfind("ccw");
    int length = input.length();
    
    if (pos_first > length)
        return 0;
    else
        return min(pos_last + 1, length - pos_first - 2);
}

int main(void)
{
    string input;
    cin >> input;
    cout << solve(input) << endl;
    return 0;
}
