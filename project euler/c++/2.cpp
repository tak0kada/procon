#include<iostream>

using namespace std;

int main() {
  int f1 = 1, f2 = 2, tmp;

  int sum_even = 0;
  while(f1 < 4000000) {
    if (f1%2 == 0) sum_even += f1;
    tmp = f1;
    f1 = f2;
    f2 = tmp + f2;
  }

  cout << sum_even << endl;
}
