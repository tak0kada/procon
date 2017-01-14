#include <iostream>
#include <string>

int main()
{
    using namespace std;
    string dna_str, rna_str;
    cin >> dna_str;
    rna_str.reserve(dna_str.size());
    
    for (size_t i = 0; i < dna_str.length(); i++)
    {
        if (dna_str[i] == 'T')
            rna_str.push_back('U');
        else
            rna_str.push_back(dna_str[i]);
    }
    
    cout << rna_str << endl;
    return 0;
}
