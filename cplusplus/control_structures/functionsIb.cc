// functionsIb.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/functions/

// Tell preprocessor to load iostream
#include <iostream>
// Tell preprocessor to load sstream
#include <sstream>
// Tell preprocessor to load strings
#include <string>

// Load standard C++ libraries
using namespace std;

// auxiliary function declaration
int multiply ( int a, int b) {

  int r;
  r = a * b;
  return r;

} //end of: int division ( int a, int b) {

// main function declaration
int main() {

  cout << "\nFunctions (I) "<< endl;
  cout << "***************"<< endl;
  
  int x=5, y=3, z;
  string myString;
  int a, b;

  z = multiply(x,y);
  
  cout << "This function takes as argument 2 numbers and returns their product " << endl;
  
  cout << "Enter the first number: " ;
  getline(cin, myString);
  stringstream(myString) >> a ;

  cout << "Enter the second number: " ;
  getline(cin,myString);
  stringstream(myString) >> b;
  
  cout << "**** " << a << " x " << b << " = " << multiply(a,b) << endl; 

 cout << "\n Program termination "<< endl;
  return 0;
   
} //end of: int main() {
