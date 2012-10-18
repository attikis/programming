// const.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/constants/

// Tell the preprocessor to include iostream standard file
#include <iostream>

// Load standard C++ libraries
using namespace std;

// function declaration
int main() {
  
  // With the "const" prefix you can declare constants with a specific type 
  // in the same way as you would do with a variable:

  const int myNumber = 100;
  const char tabulator = '\t';

  // Here, "myNumber" and "tabulator" are two typed constants. They are 
  // treated just like regular variables except that their values CANNOT 
  //  be modified after their definition.

  cout << "\nmyNumber has a value " << tabulator << myNumber << endl;
  cout << "(Notice that the \"tabulator\" character definition is working. There has been a \'tab\' inserted before 100)\n" <<endl; 

  // If I try to change its value:
  // int myNumber = 50;
  // A compilation error will occur with the message:
  // 'myNumber' has a previous declaration as 'const int myNumber'
  
  // program termination
  return 0;
  
} //end of:  int main() {


