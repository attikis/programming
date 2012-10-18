// overloaded_functions.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/functions2/

// Tell the preprocessos to include the file iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;


//Overloaded functions.
// *******************
// In C++ two different functions can have the SAME name if their parameter types or
// number are different. That means that you can give the SAME name to more than one 
// function if they have EITHER a different number of parameters OR different types in 
// their parameters.

int operate ( int a, int b) {

  return (a*b);

}  //end of: int operate ( int a, int b) {

float operate ( float a, float b) {

  return (a/b);

}  // end of: float operate ( float a, float b) {


//main function declaration
int main() {

  int x=2, y=2;
  float n = 5.0, m=2.0;

  cout << "\n" << endl;
  cout << "operate(x,y) = " << operate(x,y) << endl;
  cout << "operate(n,m) = " << operate(n,m) << endl;
  
  cout << "\n In this case we have defined two functions with the same name, \"operate\", but one of them accepts two parameters of type \"int\" and the other one accepts them of type \"float\". The compiler knows which one to call in each case by examining the types passed as arguments when the function is called. If it is called with two ints as its arguments it calls to the function that has two int parameters in its prototype and if it is called with two floats it will call to the one which has two float parameters in its prototype. " << endl;
  cout  << "\n Notice that a function cannot be overloaded only by its return type. At least one of its parameters must have a different type." << endl;
  
  cout << "\n Program Termination!" << endl;
  return 0;

} //end of: int main() {
