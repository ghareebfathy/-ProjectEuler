// Problem 21

#include <iostream>

using namespace std;
int amicable_numbers(int x);
int main()
{
    int l = 0;
    for (int i = 1 ; i < 10000; i++){
        if (amicable_numbers(i)){
            l += i;
        }
    }
    cout<<l << " ";
    

    return 0;
}
int amicable_numbers(int x){
    int sum1 = 0 , sum2 = 0 ;
    
    for (int i = 1 ; i < x ; i++){
        if (x % i == 0)
            sum1 += i;
    }
    for(int j = 1; j < sum1 ; j++){
        if (sum1 % j == 0)
            sum2+=j;
    }
    return x == sum2 && sum1 != sum2 ;
}