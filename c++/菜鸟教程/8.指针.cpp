#include <iostream>

using namespace std;

int main(){
    int var = 20;
    int *ip;// 指针变量的声明

    ip = &var;
    //指针变量的地址
    cout << "address stored in ip variable : ";
    cout << ip << endl;

    //指针中地址的值
    cout << "value of *ip variable : ";
    cout << *ip << endl;

    return 0;
}