//This is a 2D coordinate grid problem, my method of solving it was using a difference array.
//You cannot brute force this problem and plot and fill each point inside the radius of wifi with the bitrate.
//Instead, just plot two points, (positive) bitrate and (negative) bitrate, per each row that's in the coffeeshop's wireless range (y-value)
//and then run your grid through a prefix sum array and voila.
//after you're done plotting all the points. Then find the max, and find the frequency of the max.

//The tricky/annoying part of this question is the grid itself and finding the relationship between the
//x and y value that is given to the ones that correspond to your own array.

//If you're having trouble understanding this explanation, print the city_grid after every big chunk of code.

#include <iostream>
#include <math.h>  
using namespace std;

int horizontal, vertical, coffee_shops;

int main()
{
  cin.sync_with_stdio(0);
  cin.tie(0);
  
  cin >> horizontal >> vertical >> coffee_shops;
  
  int city_grid[horizontal][vertical]; //Defining the coordinate system
  int hori_displacement, verti_displacement, radius, bitrate; //The variables of each query
  float reach; //Self defined variable, very important for plotting out the points for the difference array 
  
  for (int x = 0; x < horizontal; ++x) { //Simply creating the grid and initializing each point
    for (int y = 0; y < vertical; ++y) {
      city_grid[x][y] = 0;
    }
  }
  
  if (vertical == 1) { //Edge case if the city is super skinny (1 unit long makes it hard for us to sum array) skip over this if you're reading for comprehension
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
    cin >> hori_displacement >> verti_displacement >> radius >> bitrate; //reading each query
    
      for (int x = -(radius); x <= radius; ++x) { //To make the difference array, we need to plot 2 x-values on each y-value that is encompassed by the radius
        if (x + verti_displacement <= horizontal && x + verti_displacement >= 1) {
          reach = pow((pow(radius, 2) - pow(x, 2)), 0.5); //The reach is the displacement of x (delta x) from the exact center of the circle.
                                                          //We need to calculate reach to see where we plot our x's for the difference array
          if (hori_displacement - floor(reach) < 1) { //Starting the difference array with the left x-value
            city_grid[-(verti_displacement) + horizontal -x][0] += bitrate; 
          } else { 
            city_grid[-(verti_displacement) + horizontal - x][(int)(hori_displacement - floor(reach)) - 1] += bitrate;
          }
          
          if (floor(reach + 1) + hori_displacement <= vertical) { //Ending the difference array with the right x-value (if it's on the map)
            city_grid[-(verti_displacement) + horizontal -x][(int)(floor(reach + 1) + hori_displacement) - 1] += -(bitrate);
          }
        }
      }  
    }
  }
  
  
  int max_bitrate = 0;
  
  for (int x = 0; x < horizontal; ++x) { //Now we prefix sum array the plotted points to create our final product
    for (int y = 1; y < vertical; ++y) { //With the final product, we can find the max bitrate and the frequency of the max.
      city_grid[x][y] += city_grid[x][y-1];
    }
  }
  
  if (vertical == 1) { //Finding the maximum for edge case super skinny city with width 1
    for (int x = 0; x < horizontal; ++x) {
      if (city_grid[x][0] > max_bitrate) {
        max_bitrate = city_grid[x][0];
      }
    }
  } else { //Finding the maximum for normal cases.
    for (int x = 0; x < horizontal; ++x) { 
      for (int y = 1; y < vertical; ++y) {
        if (city_grid[x][y] > max_bitrate) {
          max_bitrate = city_grid[x][y];
        }
      }
    }
  }
  
  
  int counter = 0; //Finding frequency of the max
  
  for (int x = 0; x < horizontal; ++x) {
    for (int y = 0; y < vertical; ++y) {
      if (city_grid[x][y] == max_bitrate) {
        counter += 1;
      }
    }
  } 
  
  cout << max_bitrate << "\n" << counter;
}
