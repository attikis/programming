// default_values.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/functions2/

// Tell the preprocessor to include the file iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;

// Default values in parameters.
// ****************************
// When declaring a function we can specify a default value for each of the parameters 
// it takes. This value will be used if the corresponding argument is left blank when 
// calling to the function. To do that, we simply have to use the assignment "=" 
// operator and a value for the arguments in the function declaration. If a value for 
// that parameter is NOT passed when the function is called, the default value is used, 
// but if a value IS specified this default value is ignored and the passed value is 
// used instead.

int divide ( int a, int b=2) { // variable "b" has a default value of 2

  int r; // the function's return value

  r = a/b;

  return (r);

} // end of: int divide ( int a, int b=2) {

// main function declaration
int main() {

    cout << "divide(12) = "<< divide(12) << endl; // "b" will be automatically assigned the value 2

    cout << "divide(12,3) = " << divide(12,3) << endl;


    cout << "\n Program Termination." << endl;
    return 0;
    
  } //end of: int main() {
  
