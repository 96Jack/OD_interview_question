#ifndef PERSON_H  //防止头文件重复包含
#define PERSON_H
#include <iostream>
#include <string>
using namespace std;

class Person
{
public:
    void setAge(int age);
    void setName(string name);
    void showPerson();
private:
    int myage;
    string myname;
};

#endif