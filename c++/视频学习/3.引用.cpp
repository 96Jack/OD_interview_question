#include <iostream>
using namespace std;

void test(){
    int arr[5] = {10, 20, 30, 40, 50};
    cout << sizeof(arr) << endl; //字节的大小
    cout << sizeof(arr[0]) << endl;
    // 一 直接引用
    // int (&ARR)[5] = arr;
    // 二 先定义数组类型，再用数组类型定义引用
    typedef int MY_ARR[5];
    MY_ARR &ARR = arr;

    for (int i=0; i<5; i++)
    {
        cout << ARR[i] <<" ";
    }
    cout << endl;
}
int main(){
    test();
    return 0;
}