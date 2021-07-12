#include <iostream>
#include <cmath>
using namespace std;

int remove_duplicates(int array[], int size){
  // remove duplicates from a sorted array
  int j = 0; // non duplicate index
  for (int i = 0; i < size-1; i++){
      // check for different elements
      if (array[i] != array[i+1]){
        // store different at the increasing index j
        array[j++] = array[i];
      }
    }
  array[j++] = array[size-1];
  return j;
}

int main(){

  int array[] = {1, 1, 2, 3, 4, 4, 4, 6, 7, 8, 9, 0};

  int unique = remove_duplicates(array, 12);

  for (int i = 0; i < unique; i++){

    cout << "array[" << i << "] : " << array[i] << endl;    
  }

  return 0;

}
