#include <iostream>

using namespace std;
#define MAX 3

int main(){
    int var[MAX] = {10, 20, 30};
    int *p;
    //指针中的数组地址
    p = var;
    for (int i=0;i<MAX;i++){
        // cout << "address of var["<< i << "]=";
        // cout <<p<<endl;

        // cout << "Value of var["<< i <<"]=";
        cout << *p << endl;
        //移动到下一个地址
        p++;
    }
    return 0;
}