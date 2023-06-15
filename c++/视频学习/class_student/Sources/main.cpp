#include <iostream>
#include "../Headers/person.h"

using namespace std;

void test01(){
    Person p1 =  Person("lucy", 100, 98.9f);
    cout << p1.getName() << endl;
    p1.setName("bob");
    cout << p1.getNum() << endl;
    cout << p1.getName() << endl;
    p1.showPerson();
    // p1.setName("lucy");
    // p1.setNum(2);
    // p1.setScore(98);
    // p1.getName();
    // p1.getNum();
    // p1.getScore();
    // p1.showPerson();
}
int main(){
    test01();
    return 0;
}