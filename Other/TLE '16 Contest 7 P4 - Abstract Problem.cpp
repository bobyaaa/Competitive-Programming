#include <iostream>
using namespace std;

int count(__int128 number, int pee) {
  
  while (number > 0) {
    if (number % 2 == 0) {
      number = number / 2;
    } else if (number == 3 || number % 4 == 1) {
      number = number - 1;
    } else {
      number = number + 1;
    }

    pee = pee + 1;

  }
  return pee;
}

int main()
{
  cin.sync_with_stdio(0);
  cin.tie(0);
  
  int n;
  cin >> n;
  
  for (int x = 0; x < n; ++x) {
    long long int num;
    cin >> num;
    cout << count(num, 0) << "\n";
  }
  
}
