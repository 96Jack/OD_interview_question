#include <iostream>
#include <string>
using namespace std;

int main(){
    string str1 = "runoob";
    string str2 = "google";
    string str3;
    int len;

    // 复制
    str3 = str1;
    cout << "str3 : " << str3 << endl;

    // 连接
    str3 = str1 + str2;
    cout << "str3 : " << str3 << endl;

    // 长度，大小
    len = str3.size();
    cout << "str3.size() : " << len << endl;

    return 0;

}