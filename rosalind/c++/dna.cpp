#include <iostream>
#include <string>

int main()
{
    using namespace std;
    string dna_str;
    cin >> dna_str;
    int a{0}, c{0}, g{0}, t{0};
    for (const auto i: dna_str)
    {
        if (i == 'A')      a += 1;
        else if (i == 'C') c += 1;
        else if (i == 'G') g += 1;
        else if (i == 'T') t += 1;
        else
        {
            cerr << "this input is invalid" << endl;
            return 1;
        }
    }
    cout << a << " " << c << " " << g << " " << t << endl;
    return 0;
}
