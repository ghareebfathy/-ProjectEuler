// Problem 100
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    long b = 15;
    long n = 21;
    long target = pow(10,12);
    while (n < target){
        long btemp = 3 * b + 2 * n - 2;
        long ntemp = 4 * b + 3 * n - 3;
        b = btemp;
        n = ntemp;
    }
    cout<< b;

    return 0;
}
