// functionsIIb.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/functions2/

// Tell the preprocessor to include the file iostream
#include <iostream>
// Tell the preprocessor to include the file sstream
#include <sstream>
// Tell the preprocessor to include the file string
#include <string>

// Include standard C++ libraries
using namespace std;

// this program will use a void function called "prevnext" which will
// give more than one returning value.

void prevnext(int x, int& prev, int& next) {

  prev = x - 1;
  next = x + 1;


} //end of: void prevnext(int x, int& prev, int& next) {

// main function declaration
int main() {

  int x, y, z;
  string myString;

  cout << "Enter any number: ";
  getline(cin,myString); 
  stringstream(myString) >> x;
  prevnext(x,y,z);
  cout << "The previous number is: " << y << " and the next is: " << z << endl;
  
  cout << "\nProgram termination." << endl;
  return 0;
  
} //end of: int main() { 
