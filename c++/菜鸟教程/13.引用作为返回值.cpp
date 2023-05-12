#include <iostream>
using namespace std;

double arr[5] = {1, 2.2, 3, 4.4, 5};

double& setValue(int i){
    double  &ref = arr[i];
    return ref;
}

int main(){
    // 函数的返回值是一个引用可以作为左值
    setValue(1) = 0.02;
    setValue(2) = 0.03;
    for (int i=0;i<5;i++){
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}