#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main() {
  string largest;

  for (int i=100; i<1000; i++)
    for (int j=i; j<1000; j++) {
      string k, tmp;
      k = tmp = to_string(i*j);
      reverse(tmp.begin(), tmp.end());
      if (k == tmp) 
        largest = k;
    }

  cout << largest << endl;
}
