#include <iostream>
#include <typeinfo>

using namespace std;
int main(){
    // 静态转换
    // int a = 10;
    // float b = static_cast<float>(a);
    // cout << b << endl;
    // cout << typeid(a).name()<< endl;
    // cout << typeid(b).name() << endl;

    // 动态转换
    // class Base{};
    // class   Derived : public Base{};
    // Base* ptr_base = new Derived;
    // Derived* ptr_derived = dynamic_cast<Derived*>(ptr_base);

    // 常量转换
    // const int a = 10;
    // int& r = const_cast<int&>(a);
    // cout << typeid(r).name() << endl;
    // cout << typeid(a).name() << endl;

    // 重新解释转换
    int a = 10;
    float b = reinterpret_cast<float&>(a);
    cout << typeid(b).name() << endl;

    return 0;

}