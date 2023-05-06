#include <iostream>
using namespace std;

void test(int &b){ // int &b = a;
    b = 200;
}
int main(){
    int a = 10;
    test(a);
    cout << a << endl;
}