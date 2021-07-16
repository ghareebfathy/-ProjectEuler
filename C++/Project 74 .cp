// Problem 74
#include <iostream>

using namespace std;
int FacSum(int n);
int main()
{
    int limit = 1000000;
    int result = 0;
 
    for (int i = 1; i <= limit; i++) {
        int n = i;
        int last = 0;
        int count = 0;
        while (n != last &&
               n != 169 && n != 363601 && n != 1454 &&
               n != 871 && n != 45361 &&
               n != 872 && n != 45362) {
            last = n;
            n = FacSum(n);
            count++;
        }
 
    if (count == 57 &&
       (n == 169 || n == 363601 || n == 1454))
        result++;
}
    cout<<result;

    return 0;
}
int FacSum(int n){
    int f[10]= {1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    int temp = n;
    int facsum = 0;
 
    while (temp > 0) {
        facsum += f[temp % 10];
        temp /= 10;
    }
    return facsum;
}