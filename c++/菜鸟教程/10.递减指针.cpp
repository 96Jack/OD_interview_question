#include  <iostream>

using namespace std;
const int MAX=3;

int main(){
    int arr[MAX] = {1, 2, 3};
    int *p;

    p = &arr[MAX-1];
    for (int i=0;i<MAX;i++){
        cout << *p << endl;
        p--;
    }
}
