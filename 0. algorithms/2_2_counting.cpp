#include <iostream>
using namespace std;


void swap(int &a, int &b){

  // swap function use pointers
  // to refer to the main scope,
  // not the function scope

  int temp;
  // swap values
  temp = a;
  a = b;
  b = temp;

}


int main(){

  int n, mark, count = 0;
  cout << "Enter Number of Students : "; cin >> n;
  for (int i = 1; i <= n; i++){
    cout << "Enter Mark(0 - 100) for Student " << i << " : "; cin >> mark;
    if (mark > 50) { count++; }
  }

  cout << "Number of Passing Students : " << count;

  return 0;
}
