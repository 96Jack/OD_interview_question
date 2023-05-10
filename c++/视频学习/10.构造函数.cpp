#include <iostream>
#include <string>

class Person{
public:
    Person(){
        cout << "无参的构造函数" << endl;
    }
    Person(int age,string name){
        my_age = age;
        my_name = name;
        cout << "有参的构造函数" << endl;
    }
private:
    int my_age;
    string my_name;
};

void test01(){
    Person p1;// 调用无参构造函数（默认）
    Person p2(18,"lucy");//调用有参的构造函数

}