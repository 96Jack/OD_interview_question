#include <iostream>
#include <string>

using namespace std;

class Stu{
    // 封装：隔离方法和属性；使用公有方法访问私有属性
public:
    void setName(string name){
        m_name = name;
    }
    void setAge(int age){
        m_age = age;
    }
    void myShow(){
        cout << "age :" << m_age <<", name :" << m_name <<endl;
    }
private:
    int m_age;
    string m_name;
};

// 普通对象
void testt01(){
    Stu student1;
    student1.setAge(20);
    student1.setName("lucy");
    student1.myShow();
}

// 指针对象
void test02(){
    Stu *s = new Stu;
    s->setAge(18);
    s->setName("bob");
    s->myShow();
    if (s!=NULL){
        delete  s;
        s = NULL;
    }

}
int main()
{
    // 实例化对象
    // testt01();
    test02();
    return 0;
}