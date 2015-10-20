#include<algorithm>
#include<array>
#include<cmath>
#include<iostream>

/*
次の形式の, 2次のディオファントス方程式を考えよう:

x^2 - D*y^2 = 1
たとえば D=13 のとき, x を最小にする解は 6492 - 13×1802 = 1 である.

D が平方数(square)のとき, 正整数のなかに解は存在しないと考えられる.

D = {2, 3, 5, 6, 7} に対して x を最小にする解は次のようになる:

32 - 2×22 = 1
22 - 3×12 = 1
92 - 5×42 = 1
52 - 6×22 = 1
82 - 7×32 = 1
したがって, D ≤ 7 に対して x を最小にする解を考えると, D=5 のとき x は最大である.

D ≤ 1000 に対する x を最小にする解で, x が最大になるような D の値を見つけよ.
*/

#include<algorithm>
#include<array>
#include<cmath>
#include<iostream>

using namespace std;

int main() {
  array<int, 7> X = {0};
  array<int, 7>::iterator idx;

  for (int D = 1; D <= 7; D++) {
    // Dが平方数ならディオファントス方程式を満たすxはない
    if (pow(static_cast<int>(sqrt(D)), 2) == D) {
        continue;
    }
    // Dが平方数でない場合
    for (int x = 2;;x++) {
      // オーバフロー!!!
      int t = x*x - 1;
      // xに対してyが自然数で存在するときxの値を登録する
      if (t % D == 0 && t == pow(static_cast<int>(sqrt(t/D)), 2) * D) {
        X[D-1] = x;
        break;
      }
    }
  }

  idx = max_element(X.begin(), X.end());
  cout << distance(X.begin(), idx) + 1 << endl;
  return 0;
}
