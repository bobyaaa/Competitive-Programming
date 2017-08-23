#include <iostream> 
#include <algorithm>
using namespace std;

int n;
char something;
int table[2050][2050];

int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  
  cin >> n;
  
  for (int i = 0; i < n; i++) {
    table[i][0] = 0;
    table[i][n+1] = 0; 
    for (int j = 1; j < n+1; j++) {
      cin >> something;
      if (something == '#') {
        table[i][j] = 1;
      } else {
        table[i][j] = 0;
      }
    } 
  }
  
  for (int i = n-2; i >= 0; i--) {
    for (int j = 1; j < n+1; j++) {
      if (table[i][j] == 1) {
        table[i][j] += min(min(table[i+1][j-1], table[i+1][j]), table[i+1][j+1]);
      }
    }
  }

  long long result = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 1; j < n+1; j++) {
      result = result + table[i][j];
    }
  }
  
  cout << result;
}
