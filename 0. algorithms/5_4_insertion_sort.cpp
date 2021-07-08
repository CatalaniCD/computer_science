#include <iostream>
using namespace std;

void ins(int h[],int m){
   int temp = 0, i = 0, j = 0;
   // PRECONDITION : loop from index 1 to n
   for(j = 1; j < m; j++){
        temp = h[j];
        i=j-1;
        // PRECONDITION : i prev element to j,
        // h[i] > temp ( current array element )
        // Compare i with temp to the left
        // until loop ends or pivot is found
        while(i >= 0 && h[i] > temp){
             // move value one index to the right
             // first loop moves i to index of j
             h[i+1] = h[i];
             i--;
        }
        // POSTCONDITION : i is the index with value < temp

        cout << endl << j << endl;
        // insert temp value, from index j, next to the pivot
        h[i+1] = temp;
        // print the array
        for (int i = 0; i < m; i++){
          cout << " " << h[i];
        }
        cout << "A[6]" << h[6];
      }
    // POSTCONDITION : sorted array
}
int main(){
   int A[10] = {83, 73, 66, 30, 60, 58, 15, 43, 39, 72};
   ins(A,10);
   return 0;
}
