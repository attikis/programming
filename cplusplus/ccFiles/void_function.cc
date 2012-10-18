// void_function.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/functions/

// Tell the preprocessor to load iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;


// If you remember the syntax of a function declaration:
// type name ( argument1, argument2 ...) statement
// you will see that the declaration begins with a type, that is the
// type of the function itself (i.e., the type of the datum that will be
// returned by the function with the return statement). 
// But what if we want to return no value?

// Imagine that we want to make a function just to show a message on the 
// screen. We do not need it to return any value. In this case we should use 
// the "void" type specifier for the function. This is a special specifier 
// that indicates absence of type.

// declaration of a void function (no datum returned by function)
void printMessage() {

  cout << "I am a void type function" << endl;
} // end of: void printMessage(){

// "void" can also be used in the function's parameter list to explicitly 
// specify that we want the function to take no actual parameters when it is 
// called. 
void printMssg(void){

  cout << "I also am a void-type function" << endl;
} //end of: printMssg(void){


// declaration of main function
int main(){
  
  // call the "void" type function "printMessage"
  printMessage();

  // call the other "void" type function "printMssg"
  printMssg();
  
  // program termination
  return 0;
  cout << "\nProgram termination." << endl;

} //end of: int main(){
