// Problem 91
#include <cmath>
#include <iostream>
int gcd(int a , int b){
    if (b == 0)
        return a;
    else
        return gcd(b,a % b);
}
using namespace std;

int main()
{
    int size= 50;
    int reutlt = size * size * 3;
    for (int x = 1 ; x <= size ; x++){
        for (int y = 1 ; y <= size ; y++) {
            int fact = gcd(x,y);
            reutlt += min(y * fact / x ,(size - x)*fact / y) * 2;
        }
            
    }
    std::cout << reutlt << std::endl;

    return 0;
}
