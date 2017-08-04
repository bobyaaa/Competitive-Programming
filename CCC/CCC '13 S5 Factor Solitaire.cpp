#include <iostream>
using namespace std;

int main()
{
  
  int value;
  cin >> value;
  
  int cost = 0;
  
  while (value != 1){
    for (int x = 2; x < value + 3; x++){
      if (value % x == 0){
        cost = cost + (value - (value/x))/ (value/x);
        value = value - (value/x);
        break;
        }
      }
  };
  
  
  cout << cost;
}
