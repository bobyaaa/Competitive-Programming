//Use stack, if the our inputed height is larger than the inputed height before, pop() until there are none higher
//This is because we wouldn't be able to build any bridges behind that large height, right?
//If it is less than or equal, we push() to stack.
//I'll leave the counting of how many bridges can be built to you :)
//If it's the same height, it's just a bit tricky.

//Solution by Andrew Xing

#include <iostream>
#include <sstream>
#include <deque>

using namespace std;

struct hill {
  long long value; //the height of the hill
  long long t; //how many hills behind it have the same height
}p;

int n;
long long height, total;
deque<hill> stacker;

int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  
  cin >> n;
  total = 0;
  
  for (int i = 0; i < n; i++) {
    cin >> height;
    bool same = false;
    while (!stacker.empty()) {
      if (stacker.back().value <= height) { //If the height is greater of equal to the previous hill
        total += stacker.back().t;
        if (stacker.back().value == height) {
          p = (hill){height, stacker.back().t + 1};
          same = true;
        }
        stacker.pop_back();
      } else { //If the height is less than the previous hill
        total++;
        break;
      }
    }
    //More conditions, if the height was found to be the same
    if (same) {
      stacker.push_back(p);
    } else {
      stacker.push_back((hill){height, 1});
    }
  }
  
  cout << total;
}
