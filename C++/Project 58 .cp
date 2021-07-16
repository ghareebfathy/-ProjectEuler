// Problem 58

#include <iostream>
#include <cmath>
using namespace std;
bool prime(int n);

int main()
{
    int noofprime = 3;
    int sl = 2;
    int c = 9;
    while( ((double)noofprime)/(2*sl+1) > 0.10){
        sl += 2;
        for (int i = 0 ; i < 3 ; i++){
            c+= sl ;
            if (prime(c)) noofprime++;
        }
        c += sl ;
    }
   
    cout<< sl+1 <<'\n';

    return 0;
}
bool prime(int n){
    if (n<=1)return false;
    if (n == 2) return true;
    if (n > 2 && n % 2 ==0)return false;
    int sqrt_num = floor(sqrt(n));
    for (int i = 3 ; i <= sqrt_num ; i+=2){
        if ( n % i == 0){
            return false;
        }
    }
    return true;    
}