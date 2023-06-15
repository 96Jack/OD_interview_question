#include <iostream>
#include <cstring>


using namespace std;

class Person{
public:
    int age;
    char *name;
};

void test01(){ 
    Person p1;
    p1.name = new char[6];
    strcpy(p1.name,"lucy");
    p1.age = 20;
    cout << "age: " << p1.age << " name:" << p1.name << endl;

    Person p2;
    // 深拷贝
    p2.name = new char[strlen(p1.name)+1];
    strcpy(p2.name, p1.name);
    p2.age = p1.age;
    cout << "age: " <<p2.age << " name:"<<p2.name << endl;

    if (p1.name != NULL){
        delete [] p1.name;
        p1.name = NULL;
    }

    if (p2.name != NULL){
        delete [] p2.name;
        p2.name = NULL;
    }
}

int main(){
    test01();
    return 0;
}