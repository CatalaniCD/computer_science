#include <iostream>
using namespace std;

// TEST mergeSort Algorithm
void mergeSortedSubarrays(int A[], int start, int mid, int end)
{
  int i, j, index = start;
  int B[100];

  for (i = start, j = mid; ((i < mid) || (j < end)); ) {

      // if 2halfs available
      if ((i < mid) && (j < end)) {
        // compare values in both halfs
        // half1 > half2 ( filter the xest value, and copy to the new array)
        if ( A[i] > A[j]) { B[index] = A[j]; j++;}
        else {B[index] = A[i]; i++;}
      }
      // if 1half available
           // half1
      else  if (i < mid) {B[index] = A[i]; i++;}
            // half2
            else {B[index] = A[j]; j++;}

      index++;
  }
  // copy sorted values B to array A
  for (i = start; i < end; i++) { A[i] = B[i]; }
  return;
}


void mergeSort(int A[], int start, int end)
{
  int mid;

  if (end == start + 1) { return; }
  else {
    mid = (start + end)/2;
    mergeSort(A, start, mid);
    mergeSort(A, mid, end);
    mergeSortedSubarrays(A, start, mid, end);
    return;
  }
}

int main(){

  int A[] = {11, 2, 4, 5, 8, 3, 9, 10, 11, 14, 16, 18, 101, 15, 8, 9};
  int size = 16;

  for (int i = 0; i < size; i++){
    cout << "index A[" << i << "] = " << A[i] <<endl;
  }

  mergeSort(A, 0, size);

  cout << "After mergeSort " << endl;

  // show sorted array
  for (int i = 0; i < size; i++){
    cout << "index A[" << i << "] = " << A[i] <<endl;
  }

  return 0;
}
