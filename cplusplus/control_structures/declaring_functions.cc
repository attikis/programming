// declaring_functions.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/functions2/

// Tell the preprocessor to include the file iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;

void instructions (void);
void odd (int a);
void even (int a); // remember, function variables are totally private!

// main function declaration
int main () {
  
  instructions();

  int i;
  do {
    cout << "\nType a number ( 0 to exit): " ;
    cin >> i;
    odd(i);
  } while (i!=0);
  
  cout << "\n ...And YES, zero is an even number!An even number is a number that is exactly divisible by 2. That means that when you divide by two the remainder is zero." << endl;
  
  cout <<"\n Program Termination!" << endl;
  return 0;
  
} //end of int main () {

void instructions (void) {
  
  cout << "\nDeclaring functions" << endl;
  cout << "*******************\n" << endl;
  cout << "Until now, we have defined all of the functions BEFORE the first appearance of calls to them in the source code. These calls were generally in function \"main\" which we have always left at the end of the source code. If you try to repeat some of the examples of functions described so far, but placing the function \"main\" before any of the other functions that were called from within it, you will most likely obtain compiling errors. The reason is that to be able to call a function it must have been DECLARED in some earlier point of the code, like we have done in all our examples. " << endl;
  cout << "\nBut there is an alternative way to avoid writing the whole code of a function before it can be used in main or in some other function. This can be achieved by declaring just a PROTOTYPE of the function before it is used, instead of the entire definition. This declaration is shorter than the entire definition, but significant enough for the compiler to determine its return type and the types of its parameters." << endl;
  cout << "\nIts form is:" << endl;
  cout << "type name ( argument_type1, argument_type2, ...);" << endl;
  cout << "It is identical to a function definition, except that it does not include the body of the function itself (i.e., the function statements that in normal definitions are enclosed in braces { }) and instead of that we end the prototype declaration with a mandatory semicolon (;)." << endl;
  cout << "\nThe inclusion of a name for each parameter as in the function definition is optional in the prototype declaration. For example, we can declare a function called protofunction with two int parameters with any of the following declarations:" << endl;

  cout << "int myFunction (int first, int second);" << endl;
  cout << "int myFunction (int, int );" << endl;
  cout << "******************************************************************\n" << endl;

} //end of: void instructions (void) {

void odd ( int a ) {
  
  if ( ( a%2)!=0 ) {  // modulo operator (%) returns the remainder of dividing a by 2
    cout << "Number is odd.\n" << endl;
  } else { even(a); }
  
} //end of: void odd ( int a ) {

void even ( int a) {

  if ( (a%2)==0 ) { // modulo operator (%) returns the remainder of dividing a by 2
    cout << "Number is even.\n" << endl;
  } else{ odd (a); }

} //end of: void even ( int a) {
