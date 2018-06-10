#include <stdio.h>

double k_1(xn, yn){
  return (xn + yn);
}

double k_2(xn, yn, K1, H){
  return xn + (H / 2.0) + yn + (H / 2.0) * K1;
}

double k_3(xn, yn, K2, H){
  return (xn + (H/2.0) + yn + (H/2.0) * K2);
}

double k_4(xn, yn, K3, H){
  return (xn + H + yn + H * K3);
}

double FI(K1, K2, K3, K4){
  return (1.0/6.0 * (K1 + 2.0 * K2 + 2.0 * K3 + K4));
}

/* int main(){ */
/*   double x0 = 0, y0 = 1; */
/*   double step = 10; */
/*   double h; */
/*   h = 1 / step; */
/*   printf("%f\n", h); */
/*   int i; */
/*   double x ,y; */
/*   x = x0; */
/*   y = y0; */
/*   double k1, k2, k3, k4; */
/*   double fi; */
  
/*   for (i = 0 ;i < step ; i++){ */
/*     k1 = k_1(x, y); */
/*     printf("k1= %f\n", k1); */
/*     k2 = k_2(x, y, k1, h); */
/*     printf("k2= %f\n", k2); */
/*     k3 = k_3(x, y, k2, h); */
/*     printf("k3= %f\n", k3); */
/*     k4 = k_4(x, y, k3, h); */
/*     printf("k4= %f\n", k4); */
/*     fi = FI(k1, k2, k3, k4); */
/*     printf("x = %f,  y = %f\n", x, y); */
/*   } */
/* } */
int main(){
  double x = 0;
  double y = 1;
  double k1, k2, k3 ,k4;
  double fi;
  double h = 0.1;
  k1 = k_1(x, y);
  k2 = k_2(x, y, k1, h);
  printf("k2 = %f\n",k2);
}
