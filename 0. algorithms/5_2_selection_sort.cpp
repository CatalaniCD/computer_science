#include <iostream>
using namespace std;


void selection_sort(int A[], int size){

  // Selection Sort
  // Its like a nested linear Search
  // Outer Loop, Swap loop
  // Inner Loop, Linear Search for max or min value ( or any comparator )

  // swap value to first
  int i, j, temp = 0;
  for (i = 0; i < size; i++){
    // linear search
    int index = i;
    for ( j = i; j < size; j++){

      // < filters max or min value
      // Update max / min index
      // Compare against the ith_est ( highest or lowest) index
      // A[index] is always the x_est index
      if (A[j] < A[index]){ index = j;}
      }

    // swap filtered value
    temp = A[i]; // store value
    A[i] = A[index]; // filter assign
    A[index] = temp; // assign stored value

    // cout << "Array index i :" << A[i] << endl;
  }

}


int main(){

  int A[] = {11, 2, 4, 5, 8, 3, 9, 10, 11, 14, 16, 18, 101, 15, 8, 9};
  int size = 16;
  // show array
  for (int i = 0; i < size; i++){
    cout << "index A[" << i << "] = " << A[i] <<endl;
  }

  selection_sort(A, size);

  cout << "after selection_sort " << endl;

  // show sorted array
  for (int i = 0; i < size; i++){
    cout << "index A[" << i << "] = " << A[i] << endl;
  }

  return 0;
}
