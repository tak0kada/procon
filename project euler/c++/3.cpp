#include <iostream>

using namespace std;

int main() {
  long p = 600851475143;
  long factor;

  for (int i=2; i*i < p; i++)
    while (p%i==0) {
      factor = i;
      p /= factor;
    }

  cout << p << endl;
}
