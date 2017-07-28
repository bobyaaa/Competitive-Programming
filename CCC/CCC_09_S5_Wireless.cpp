#include <iostream>
#include <math.h>  
using namespace std;

int horizontal, vertical, coffee_shops;

int main()
{
  cin.sync_with_stdio(0);
  cin.tie(0);
  
  cin >> horizontal >> vertical >> coffee_shops;
  
  int city_grid[horizontal][vertical];
  int hori_displacement, verti_displacement, radius, bitrate;
  float reach;
  
  for (int x = 0; x < horizontal; ++x) {
    for (int y = 0; y < vertical; ++y) {
      city_grid[x][y] = 0;
    }
  }
  
  if (vertical == 1) {
    for (int i = 0; i < coffee_shops; ++i) {
    cin >> hori_displacement >> verti_displacement >> radius >> bitrate;
    
      for (int x = -(radius); x <= radius; ++x) {
        if (x + verti_displacement <= horizontal && x + verti_displacement >= 1) {
          city_grid[-(verti_displacement) + horizontal -x][0] += bitrate;
        }
      }
    }
  } else {
    for (int i = 0; i < coffee_shops; ++i) {
    cin >> hori_displacement >> verti_displacement >> radius >> bitrate;
    
      for (int x = -(radius); x <= radius; ++x) {
        if (x + verti_displacement <= horizontal && x + verti_displacement >= 1) {
          reach = pow((pow(radius, 2) - pow(x, 2)), 0.5);
          
          if (hori_displacement - floor(reach) < 1) {
            city_grid[-(verti_displacement) + horizontal -x][0] += bitrate;
          } else {
            city_grid[-(verti_displacement) + horizontal - x][(int)(hori_displacement - floor(reach)) - 1] += bitrate;
          }
          
          if (floor(reach + 1) + hori_displacement <= vertical) {
            city_grid[-(verti_displacement) + horizontal -x][(int)(floor(reach + 1) + hori_displacement) - 1] += -(bitrate);
          }
        }
      } 
    }
  }
  
  
  int max_bitrate = 0;
  
  for (int x = 0; x < horizontal; ++x) {
    for (int y = 1; y < vertical; ++y) {
      city_grid[x][y] += city_grid[x][y-1];
    }
  }
  
  if (vertical == 1) {
    for (int x = 0; x < horizontal; ++x) {
      if (city_grid[x][0] > max_bitrate) {
        max_bitrate = city_grid[x][0];
      }
    }
  } else {
    for (int x = 0; x < horizontal; ++x) {
      for (int y = 1; y < vertical; ++y) {
        if (city_grid[x][y] > max_bitrate) {
          max_bitrate = city_grid[x][y];
        }
      }
    }
  }
  
  
  int counter = 0;
  
  for (int x = 0; x < horizontal; ++x) {
    for (int y = 0; y < vertical; ++y) {
      if (city_grid[x][y] == max_bitrate) {
        counter += 1;
      }
    }
  } 
  
  cout << max_bitrate << "\n" << counter;
}