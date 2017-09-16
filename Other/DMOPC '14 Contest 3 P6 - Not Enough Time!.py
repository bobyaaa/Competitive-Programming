#include <iostream>
#include <algorithm>

using namespace std;

long long dp[10500];
long long dp2[10500];
int n, t;
int ppoor, vpoor, paverage, vaverage, pgood, vgood;

int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
    
  cin >> n >> t;
  
  for (int i = 0; i < t+1; i++) {
    dp[i] = 0;
    dp2[i] = 0;
  }
  
  for (int i = 0; i < n; i++) {
    cin >> ppoor >> vpoor >> paverage >> vaverage >> pgood >> vgood;
    for (int j = 1; j < t+1; j++) {
      
      long long check[4]; //Take not take take not take take not take.
      
      for (int x = 0; x < 4; x++) {
        check[x] = 0;
      }
      
      if (j >= ppoor) {
        check[0] = vpoor + dp[j-ppoor]; //We take
        check[1] = dp[j];//We don't take
      } else {
        check[1] = dp[j]; //We don't take
      }
      
      if (j >= paverage) {
        check[2] = vaverage + dp[j-paverage];
      }
      
      if (j >= pgood) {
        check[3] = vgood + dp[j-pgood];
      }
      
      int max = 0;
      
      for (int x = 0; x < 4; x++) {
        if (check[x] > max) {
          max = check[x];
        }
      }
      
      dp2[j] = max;
      
    //Something for the flip? Think about it!
    }
    swap(dp, dp2);
  }
  
  cout << dp[t];
  
}
