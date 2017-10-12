//Did you know that using endl for a large printing question makes the cpp code slower than python??
#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int rows, cols, query;
int thisCol, thisRow;
string input;
bool checkerRow[1002]; 
bool checkerCol[1002];

int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  cin >> rows >> cols;
  
  for (int i = 0; i < rows; i++) {
    cin >> input;
    for (int j = 0; j < cols; j++) {
      if (input.at(j) == 'X') {
        checkerCol[j] = true;
        checkerRow[i] = true;
      }
    }
  }
  
  cin >> query;
  
  for (int i = 0; i < query; i++) {
    cin >> thisCol >> thisRow;
    
    if (checkerRow[thisRow-1] == true || checkerCol[thisCol-1] == true) {
      cout << 'Y';
    } else {
      cout << 'N';
    }
    
    cout << "\n";
  }
}
