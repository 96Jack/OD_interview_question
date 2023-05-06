#include <iostream>
#include <string>

using namespace std;

// 1. 整型数据空间的申请和释放
void test01(){
    // 默认给值100
    int *p = new int(100);
    cout << "*p :" << *p << endl;

    //释放空间
    if (p != NULL){
        delete p;
        p = NULL;
    }
}

// 2. 数组空间的申请和释放
void test02(){
    int *arr = new int[5];
    for (int i=0; i<5; i++){
        arr[i] = 100+i;
        cout << arr[i] << " ";
    }
    cout <<endl;

    // 释放数组空间
    if (arr != NULL){
        // 注意[], 表示释放的是数组
        delete [] arr;
        arr = NULL;
    }
}

// 3. 结构体空间的申请和释放
struct Stu{
    int num;
    string name;
};

void test03(){
    Stu *p = new Stu;
    p -> name = "lucy";
    p -> num = 100;
    cout << "num :" << p->num <<" ,name:" << p->name<< endl;

    // 释放
    if (p != NULL){
        delete p;
        p = NULL;
    }
}

int main(){
    // test01();
    // test02();
    test03();
}