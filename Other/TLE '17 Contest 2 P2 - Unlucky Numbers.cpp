//Store all values in their relative index and prefix sum array. Alternatively, storing, sorting and prefix sum array
//Still manages to pass the time restraints on python2.
//Solution by Andrew Xing

#include <iostream>
#include <string>
using namespace std;

int main() {
    
    cin.sync_with_stdio(0);
    cin.tie(0);
    
    int arr[1000050] = { 0 };
    
    int K;
    cin >> K;

    int x;
    for (int i = 0; i < K; i++) {
        cin >> x;
        arr[x] = 1;
    }
    
    for (int i = 1; i < 1000050; i++) {
        arr[i] += arr[i-1];
    }
    
    int N;
    cin >> N;
    
    int f;
    for (int i = 0; i < N; i++) {
        cin >> f;
        cout << f - arr[f] << "\n";
    }
    
}
