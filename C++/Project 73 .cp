// Problem 73

#include <iostream>

using namespace std;
int hcfnaive(int a,int b);
int main()
{
    int a = 3;
    int b = 2;
    int limit = 12000;
    int result = 0;
    for (int d = 5; d <= limit; d++) {
    for (int n = d / a + 1; n < (d - 1) / b + 1; n++) {
        if (hcfnaive(n, d) == 1) result++;
    }
}

    cout<<result;
    return 0;
}
int hcfnaive(int a,int b){
    if (b == 0) 
        return a ;
    else 
        return hcfnaive(b,a % b);
}