//Beautiful explanation at: https://amorim.ca/display/CS/Circle+of+Life
//I can't say it any better (except maybe the power of 2 thing), which I still don't fully understand

//Solution by Andrew Xing

#include <iostream>
#include <cmath>
using namespace std;

long long n, t;
bool chart[100050];
bool newChart[100050];
char cell;

int shiftAndWrap(int currentPosition, int arraySize, long long shift) {
    
    long long nonCyclicIndex = (currentPosition + shift) % arraySize;
    
    if (nonCyclicIndex < 0)
        return arraySize + nonCyclicIndex;
    else
        return nonCyclicIndex;
}

int main() {
  
  cin >> n >> t;
  
  for (int i = 0; i < n; i++) {
    cin >> cell;
    if (cell == '0') {
      chart[i] = false;
    } else {
      chart[i] = true;
    }
  }
  
  long long largestpoweroftwo = 1;
  int power = 0;
  
  while (t > 0) {
    //Find the largestpoweroftwo
    largestpoweroftwo = 1;
    while (largestpoweroftwo <= t) {
      if (pow(2, power) <= t) {
        largestpoweroftwo = pow(2, power);
        power++;
      } else {
        break;
      }
    } 
    
    power = 0;
    t = t - largestpoweroftwo;
    //Some code that shifts the thing goes here
    for (int i = 0; i < n; i++) {
      newChart[i] = chart[shiftAndWrap(i, n, largestpoweroftwo)] ^ chart[shiftAndWrap(i, n, -largestpoweroftwo)];
    }
    
    for (int i = 0; i < n; i++) {
      chart[i] = newChart[i];
    }
    
    //Then here we calculate how far it goes down using the largest power of 2 on the n thing..
  }
  
  for (int i = 0; i < n; i++) {
    cout << newChart[i];
  }
}
