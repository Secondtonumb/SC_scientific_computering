#include <stdio.h>
#include <math.h>

int main(){
  double i = 1;
  int m;
  for(m = 0; m < 10; m++){
    i = (pow(i , 2) + 1) / (2 * i -1);
    printf("Iteration [%d] : %0.50f\n",m + 1, i);
  }
}
