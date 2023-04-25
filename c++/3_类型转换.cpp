#include <iostream>
#include <typeinfo>

using namespace std;
int main(){
    int a = 10;
    float b = static_cast<float>(a);
    cout << b << endl;
    cout << typeid(a).name()<< endl;
    cout << typeid(b).name() << endl;
    return 0;

}