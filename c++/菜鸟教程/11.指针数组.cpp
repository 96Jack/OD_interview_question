#include <iostream>

using namespace std;
#define MAX 3

int main(){
    int arr[MAX] = {1, 2, 3};
    int *p[MAX];

    for (int i=0;i<MAX;i++){
        p[i] = &arr[i];
        cout << *p[i] << endl;
    }
    return 0;
}
