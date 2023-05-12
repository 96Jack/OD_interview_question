#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int t1(){
    char c;
    // 用来获取第一字符
    cin.get(c);
    cout << c << endl;
    return 0;
}
void t2(){
    char c[5];
    // 输入的时候回车符会占一个字符，输出会少一个字符;要比预期输入多设置一个字符
    // 12345 >> 1234
    cin.get(c, 5);
    cout << c << endl;

}
void t3(){
    char c[20];
    // 默认换行结束
    // cin.getline(c,4);
    //指定结束符号 : 12/34 >> 12
    cin.getline(c,4,'/');
    cout << c << endl;
}

void t4(){
    string str;
    getline(cin,str);
    cout << str << endl;
}
void t5(){
    char c = tolower(getchar());
    cout << c << endl;
}
void t6(){
    string str,s[100];int n;int i=0;
	cin >> n;cin.get();
	for(int i = 0; i < n; i++){
		getline(cin,str);
		s[i] = str;
	}
	for(int i = 0; i < n; i++){
        cout << s[i] << endl;
	}
}
int main(){
    // t1();
    // t2();
    // t3();
    // t4();
    // t5();
    t6();
}