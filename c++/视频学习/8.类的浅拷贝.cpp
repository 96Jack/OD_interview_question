#include <iostream>
#include <cstring>
using namespace std;

class Person{
public:
    char *name;
    int age;
};

void test01(){
    Person p1;
    p1.name = new char[16];//从堆区申请
    strcpy(p1.name, "lucy");
    p1.age = 20;
    cout << p1.age << " " << p1.name << endl;

    Person p2;
    p2 = p1;
    cout << p2.age << " " << p2.name << endl; 
    // 浅拷贝
    if (p1.name != NULL){
        delete [] p1.name;
        p1.name = NULL;
    }
    // if (p2.name != NULL){
    //     delete [] p2.name;
    //     p2.name = NULL;
    // }
}

int main(){
    test01();
    return 0;
}