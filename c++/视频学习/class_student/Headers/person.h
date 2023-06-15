#ifndef PERSON_H  //防止头文件重复包含
#define PERSON_H
#include <iostream>
#include <string>
using namespace std;

class Person
{
public:
    // 无参构造
    Person();
    // 有参构造
    Person(const char *name , int num, float score);
    // 析构函数
    ~Person();

    // 设置数据
    void setName(const char *name);
    void setNum(int num);
    void setScore(float score);

    // 获取数据
    char *getName();
    int getNum();
    float getScore();

    // 显示数据
    void showPerson();
private:
    char *m_Name;
    int m_Num;
    float m_Score;
};

#endif