#include <iostream>
using namespace std;

namespace A{
    int num = 10;
    namespace B{
        int num = 20;
    }
}
int main(){
    cout << A::num << endl;
    cout << A::B::num << endl;
    return 0;
}