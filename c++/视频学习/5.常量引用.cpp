#include <iostream>
using namespace std;

struct STU{
    int num;
    char name[32];
};

// 此时的temp == lucy 是 4+32=36个字节
// void showSTU(STU temp){
//     cout << temp.num<< " " << temp.name << endl;
// }

// 使用常量引用后，4个字节,节省空间
void showSTU(const STU &temp){
    cout << "name : " << temp.name << endl << "age : " << temp.num << endl;
}

int main(){
    // 常量引用;给常量取别名
    const int &b = 10;
    // 常量引用的应用
    STU lucy = {100, "lucy"};
    showSTU(lucy);
}