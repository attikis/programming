// defined_constants.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/constants

// Tell the preprocessor to include the iostream standard file
#include <iostream>

// Load standard C++ libraries
using namespace std;

// You can define your own names for constants that you use very often 
// without having to resort to memory-consuming variables, simply by using 
// the #define preprocessor directive. Its format is:
// #define identifier value
// See example below:

#define PI 3.14159
#define mTop 172.5
#define newLine '\n'
// Once they are defined, constnat can be used in the rest of the code as if 
// they were any other regular constant
// Note: The #define directive is not a C++ statement but a directive for 
// the preprocessor; therefore it assumes the entire line as the directive and
// does not require a semicolon (;) at its end. If you append a semicolon 
// character (;) at the end, it will also be appended in all occurrences 
// within the body of the program that the preprocessor replaces
int main() {

  cout << "PI = " << PI << newLine << "mTop = " << mTop << endl; 

  int R = 1;
  int newR = 3;
  cout << newLine << "A circle with Radius (R) = "<< R << " has circumference " << 2*PI*R << ",\n whereas a circle with Radius(R) = " << newR << " has circumference "<< 2*PI*newR << ".\n" << endl;

  // program termination 
  return 0;
  } // end of: int main() {
