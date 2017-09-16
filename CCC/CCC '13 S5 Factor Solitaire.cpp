//I'm not 100% sure how this works myself, but working backwards is the key to this problem. Divide by the lowest number possible that
//is not the number 1, and if your number is prime, then just accept it.

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
