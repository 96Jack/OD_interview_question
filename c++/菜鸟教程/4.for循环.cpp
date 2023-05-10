#include <iostream>
#include <string>
#include <cctype>


using namespace std;

int arry[5] = {1, 2, 3, 4, 5};

// c++11
int main(){
    // 一，不会改变arry的值
    // 二，会改变arry的值，&表示对arry中的值的引用
    for (int x : arry){
    // for (int &x : arry){
    // for (auto &x : arry){
        x += 2;
        cout << x;
    }
    cout << endl;
    for (int x=0; x<5;x++){
        cout << arry[x];
    } 
    cout << endl;
    string str("some thing");
    for (auto &c : str){
        c = toupper(c);
    }
    cout << str << endl;
    return 0;
}