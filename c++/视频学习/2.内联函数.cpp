#include <iostream>
using namespace std;
inline int my_func(int a, int b)
{
    return a<b?a:b;
}
int main(){
    int a=10;
    int b=20;
    cout << my_func(++a, b) << endl;
}