#include<iostream>

using namespace std;

int main(){
  cout << "Insertion Sort." << endl;
  
  int A[10] = {4,6,2,4,9,1,5,2,8,3};
  int curr = 0;
  int i = 0;

  for(int j = 1; j < 10; j++) {
    curr = A[j];
    i = j-1;

    while(i >= 0 && A[i] > curr){
      A[i+1] = A[i];
      i--;
    }
    A[i+1] = curr;
  }

  for(int k = 0; k<10; k++){
    cout << A[k] << " ";
  }
  return 0;
}
