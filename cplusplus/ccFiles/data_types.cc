// data_types.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/variables/

// "signed" types can represent both positive and negative values
// whereas "unsigned" types can only represent positive values (and zero). 
// This can be specified by using either the specifier "signed" or the specifier 
// "unsigned" before the type name. 
// By default, if one does not  specify whether the variable is signed or unsigned 
// most compiler settings will assume the type to be signed.

#include <iostream>
// load standard C++ libraries
using namespace std;

// function declaration
int main() {

  // Declare variables here. These are local variables (difined within main() )
  int a, b;
  int result;
  // A variable can be either of "global" or "local" scope. 
  // A "global" variable is a variable declared in the main body of the source code,
  // outside all functions. A "local" variable is one declared within the body of 
  // a function or a block.
  // "Global" variables can be referred from anywhere in the code, even inside 
  // functions, whenever it is after its declaration. "Local" variables
  // declared inside a function cannot be accessed from other functions

  // Calculations here
  a = 5;
  b = 2;
  a = a + 1;

  result = ( a-b );
  
  // Print out the result:
  cout << "result is : " << result << endl;

  // programme termination
  return 0;

} //end of: int main (){
