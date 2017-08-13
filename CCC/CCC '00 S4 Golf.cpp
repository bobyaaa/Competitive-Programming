//Using DP tables, really disgusting method. I literally had no idea what I was doing, and I magically got the answer.
//What the heck. Literally did not know what I did right. Just randomly sorted things and reversed them. wow.
//Go to the python solution, it's much better (and it's fixed).
//Solution by Andrew Xing

#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int clubs;
int table[40][6000][2]; //Approximations
int items[40];

int main() {
  
  int distance;
  cin >> distance;
  cin >> clubs;
  for (int x = 0; x < clubs+2; x++) {
    for (int y = 0; y < distance+2; y++) {
      table[x][y][0] = 0;
      table[x][y][1] = 0;
    }
  }
  
  for (int x = 0; x < clubs; x++) {
    cin >> items[x];
  }
 
  std::sort(items, items + clubs, std::greater<int>());
 
  for (int i = 1; i < clubs+1; i++) {
    int club = items[i-1];
    for (int j = 1; j < distance + 1; j++) {
      if (club <= j) {
        if (club + table[i][j-club][0] > table[i-1][j][0]) {
          table[i][j][0] += club + table[i][j-club][0];
          if (table[i][j][0] == table[i-1][j][0]) {
            if (table[i][j-club][1] + 1 < table[i-1][j][1]) {
              table[i][j][1] = 1 + table[i][j-club][1];
            } else {
              table[i][j][1] = table[i-1][j][1];
            }
          } else {
            table[i][j][1] = 1 + table[i][j-club][1];
          }
        } else {
          table[i][j][0] = table[i-1][j][0];
          table[i][j][1] = table[i-1][j][1];
        }
      } else {
        table[i][j][0] = table[i-1][j][0];
        table[i][j][1] = table[i-1][j][1];
      }
    }
  }
  
  
  if (table[clubs][distance][0] == distance) {
    cout << "Roberta wins in " << table[clubs][distance][1] << " strokes.";
  } else {
    cout << "Roberta acknowledges defeat.";
  }
}
