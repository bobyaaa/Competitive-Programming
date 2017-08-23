//2D prefix sum array into brute forcing all possible rectangles
//Solution by Andrew Xing

#include <iostream>

using namespace std;

int W, H, area;

long long scales;
long long grid[275][275]; //Just in case they lie about the parameters a little

int main() {
  cin.sync_with_stdio(0);
  cin.tie(0);
  
  cin >> W >> H >> area;
  
  for (int y = 0; y < H+1; y++) { //Adds edges for easier calculations
    grid[y][0] = 0;
  }
  
  for (int x = 0; x < W+1; x++) {
    grid[0][x] = 0;
  }
  
  for (int y = 1; y < H+1; y++) { //Cin >> values;
    for (int x = 1; x < W+1; x++) {
      cin >> grid[y][x];
    }
  }
  
  for (int y = 1; y < H+1; y++) { //Prefix sum array
    for (int x = 2; x < W+1; x++) {
      grid[y][x] += grid[y][x-1];
    }
  } 
  
  for (int y = 2; y < H+1; y++) {
    for (int x = 1; x < W+1; x++) {
      grid[y][x] += grid[y-1][x];
    }
  }
  
  //Now we try to brute force all the rectangles given the rectangle sizes
  int result = 0;
  
  if (area >= W*H) {
    cout << grid[H][W];
  } else {
    
    int width, height;
    height = 300; 
    width = 1;
    
    while (width < height) {
      height = area/width;

      for (int i = height; i < H+1; i++) {
        for (int j = width; j < W+1; j++) {

          if (grid[i][j] - grid[i-height][j] - grid[i][j-width] + grid[i-height][j-width] > result) {
            result = grid[i][j] - grid[i-height][j] - grid[i][j-width] + grid[i-height][j-width];
          }
        } 
      }
      
      int temp_save;
      temp_save = height;
      height = width;
      width = temp_save;
      
      for (int i = height; i < H+1; i++) {
        for (int j = width; j < W+1; j++) {
          if (grid[i][j] - grid[i-height][j] - grid[i][j-width] + grid[i-height][j-width] > result) {
            result = grid[i][j] - grid[i-height][j] - grid[i][j-width] + grid[i-height][j-width];
          }
        } 
      }
      
      temp_save = height;
      height = width;
      width = temp_save;
      
      width = width + 1;
    }
    
    for (int widt = 1; widt < (area/2)+2; widt++) {
      width = widt;
      height = area/widt;
      
      height = 1;
      width = 1;
      
      if (height >= H) {
        height = 1; 
      }
      
      if (width >= W) {
        width = 1;
      }
      //Great, now we have to shove each premade square into the grid;
      
      
    }
      
  cout << result;
  } 
  
}
