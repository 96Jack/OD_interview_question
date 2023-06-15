#include "../Headers/person.h"
#include <iostream>
#include <cstring>

using namespace std;
 
Person::Person()
{
    cout << "无参构造" << endl; 
}
// :之后是初始化列表
Person::Person(const char *name , int num=0, float score=0.0f)
{
    cout << "有参构造" << endl;
    m_Name = new char[strlen(name)+1];
    strcpy(m_Name,name);
    m_Num = num;
    m_Score = score;
}
Person::~Person(){
    cout << "析构函数" << endl;
    if (m_Name != NULL){
        delete [] m_Name;
        m_Name = NULL;
    }
}

void Person::setName(const char *name){
    // 释放旧的空间
    if (m_Name != NULL){
        delete [] m_Name;
        m_Name = NULL;
    }

    // 根据形参，重新申请空间
    m_Name = new char[strlen(name)+1];
    strcpy(m_Name,name);
    

}
void Person::setNum(int num){
    m_Num = num;
}
void Person::setScore(float score){
    m_Score = score;
}
// 获取数据
char *Person::getName(){
    return m_Name;
}
int Person::getNum(){
    return m_Num;
}
float Person::getScore(){
    return m_Score;
}
// 显示数据
void Person::showPerson(){
    cout << "name: " << m_Name << " num: " << m_Num << " score: "<< m_Score << endl;
}
