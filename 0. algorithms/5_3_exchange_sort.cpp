#include <iostream>
using namespace std;

void bubbleSort (int A[], int n) {
  // PRECONDITION : iterate index [from 0 to size -1]
  for (int i=0; i<n-1; i++) {
    // PRECONDITION : iterate index [from size - 1 to i]
    for (int j=n-1; j>i; j--) {
      // Evaluate values j < j-1
      if (A[j] < A[j-1]) {
        // swap values
        int temp=A[j];
        A[j]=A[j-1];
        A[j-1]=temp;
      }
      // else, theres no swap
    }
    // POSTCONDITION : smallest value swapped to left Part
    // or to the i index
  }
  // POSTCONDITION : array sorted, increasing order
}

int myFunction(int arr[], int n, int x, int low, int high){
  // BinarySearch
  int var=-1;
  int mid;
  // PRECONDITION : low <= high
  while (low <= high){
    // array midpoint
    mid=(low+high)/2;
    // check if mid value is element
    if (arr[mid]==x){
      var=mid;
      low=mid+1;
    }
    // check if element < mid value
    else if (arr[mid]>x)
      high=mid-1;
    // element > mid value
    else
      low=mid+1;
    // each iteration makes low + 1, high -1
    // Termination case low > high
  }
  // POSTCONDITION : element found or not
  // var value, is the value for the bisection
  return var;
}

/*
sorted array : { 3,3,4,7,7,8,8,10 }

iterations :
1. mid = (0 + 7) / 2 -> 3
  array[3] == 7, 7 == 8 ?
  7 > 8 False, low = 3 + 1
2. mid = (4 + 7) / 2 -> 5
  array[5] == 8, 8 == 8 ?
  var = 5, low = 5 + 1
3. mid = (6 + 7) / 2 -> 6
  array[6] == 8, 8 == 8 ?
  var = 6, low = 6 + 1
6. low > high

*/
int main(){
  int arr[]={8,7,10,3,3,8,7,4};
  int n=8; //size of array
  bubbleSort(arr,n);
  int output=myFunction(arr,n,8,0,n-1);
  cout<<output;
  return 0;
}
