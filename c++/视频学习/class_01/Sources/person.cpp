#include "../Headers/person.h"
#include <iostream>
#include <string>
using namespace std;

void Person::setAge(int age)
{
    myage = age;
}
void Person::setName(string name)
{
    myname = name;
}
void Person::showPerson()
{
    cout << "age=" <<myage <<"; name="<< myname<<endl;
}