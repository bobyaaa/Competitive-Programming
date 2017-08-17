//It's a two part problem. The basic concept we need to know before tackling the problem is finding the maximum 
//rectangular area under a histogram. Then we gotta apply it to a grid.
//Go on youtube and look at https://www.youtube.com/watch?v=ZmnqCZp9bBs
//then look at https://www.youtube.com/watch?v=g8bSdXCG-lA&t=344s

//Solution by Andrew Xing

#include <iostream>
#include <stack>
#include <stdio.h>

using namespace std;
int n;
int rows;
int cols;
char theDanker;
int swaglist[1050];

int maxAreaHistogram(int list[], int size) {
  std::stack<int> position;
  int maxArea = 0; //Formula = size*(currentPosition - savedPosition) or (size*i)
  int area = 0;
  int save;
  int dank = 0;
  
  while (dank < size) {
    
    if (position.empty() || list[dank] >= list[position.top()]) {
      position.push(dank++);
    } else {
      save = position.top();
      position.pop();
  
      if (position.empty()) {
        area = list[save] * dank;
      } else {
        area = list[save] * (dank - position.top() -1);
      }
      
      if (area > maxArea) {
          maxArea = area;
      }
    }
  }

  while (position.empty() == false) {
    save = position.top();
    position.pop();
    
    if (position.empty()) {
      area = list[save] * dank;
    } else {
      area = list[save] * (dank - position.top() -1);
    }
    
    if (area > maxArea) {
        maxArea = area;
    }
  } 
    
  return maxArea;
}

int main() {
  //scanf does not work with cin with fast input.
  cin.sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  
  for (int x = 0; x < n; x++) {
    int maximum = 0;
    for (int i = 0; i < cols; i++) {
      swaglist[i] = 0;
    }
    
    cin >> rows >> cols;
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        cin >> theDanker;
        if (theDanker == 'F') {
          swaglist[j] = swaglist[j] + 1;
        } else { // theDanker == "R"
          swaglist[j] = 0;
        }
      }
      int woohoo = maxAreaHistogram(swaglist, cols) * 3;
      if ( woohoo > maximum) {
        maximum = woohoo; 
      }
    }
    cout << maximum << "\n"; 
  }
}
