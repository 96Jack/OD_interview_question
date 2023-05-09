#include <iostream>
#include "../Headers/person.h"

using namespace std;

void test01(){
    Person p1;
    p1.setAge(18);
    p1.setName("lucy");
    p1.showPerson();
}
int main(){
    test01();
    return 0;
}