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

  int a;
  int b;
  cout << "Enter 'a' value : "; cin >> a;
  cout << "Enter 'b' value : "; cin >> b;
  cout << "Value for a, b : " << a << ", " << b << endl;
  cout << "Swaping values..." << endl;
  swap(a, b);
  cout << "Value for a, b : " << a << ", " << b << endl;
  return 0;
}
