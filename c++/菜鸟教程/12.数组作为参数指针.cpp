#include <iostream>
using namespace std;

double getAverge(int *arr, int size);

double getAverge(int *arr, int size){
    int i, sum = 0;
    double avg;
    for (i = 0;i < size;i++){
        sum += arr[i];
    }
    avg = double(sum)/size;
    return avg;
}

int main(){
    int blances[5] = {1000, 2, 13, 4, 17};
    double avg;

    avg = getAverge(blances,5);
    cout <<"Average value is : " << avg << endl;
    return 0;
}