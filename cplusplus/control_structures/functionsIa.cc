// functionsIa.cc
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
int addition ( int a, int b) {
  
  int r;
  r = a + b;
  
  return r; 
  // "return r;" finalizes function addition, and returns the control back 
  // to the function that called it in the first place (in this case, main). 
  // At this moment the program follows it regular course from the same point 
  // at which it was interrupted by the call to addition
  
} //end of: int addition( int a, int b) {

// main function declaration
int main() {

  cout << "\nFunctions (I) "<< endl;
  cout << "***************"<< endl;
  
  // A "function" is a group of statements that is executed when it is called 
  // from some point of the program. The following is its format:
  
  // type name (parameter1, parameter2, ..., parameterN) {statements}
  
  // "type" is the data type specifier of the data RETURNED by the function.
  // "name" is the identifier by which it will be possible to call the function.
  // "parameters" (as many as needed): Each parameter consists of a data type 
  // specifier followed by an identifier, like any regular variable declaration 
  // (for example: int x) and which acts within the function as a regular 
  // local variable. They allow to pass arguments to the function when it is 
  // called. The different parameters are separated by commas.
  // "statements" is the function's body. It is a block of statements surrounded 
  // by braces { }.

  cout << "\nReminder: a C++ program always begins its execution by the main() function, no matter where it is positioned inside the code!" << endl;
 
  int z;
  z = addition (5,3); // calls the function "addition" giving it the 
                      // two arguments it requires for execution. 
                      // It returns r = a+b, whose value is then assigned to 
                      // the integer "z".

  cout << "\nThe result is " << z << endl;
 
  string myString;
  int firstNum;
  int secNum;
  int result;
  
  cout << "\n *Please insert any number: " ;
  getline(cin,myString); // input number
  stringstream(myString) >> firstNum;

  cout << " **Please insert another number: " ;
  getline(cin,myString); // input number
  stringstream(myString) >> secNum;

  result = addition(firstNum, secNum);
  cout << " *** Adding these two numbers gives "<< result << "." << endl;

  // The parameters and arguments have a clear correspondence.Within the "main"
  // function we called to "addition" passing two values: 5 and 3, that 
  // correspond to the "int a" and "int b" parameters declared for function 
  // "addition". At the point at which the function is called from within 
  // "main", the control is LOST by "main" and passed to function "addition". 
  // The value of both arguments passed in the call (5 and 3) are COPIED to 
  // the local variables  "int a" and "int b" within the function "addition".
  // Function "addition" declares another local variable (int r), and by means
  // of the expression r=a+b, it assigns to r the result of "a" plus "b". 
  // Because the actual parameters passed for "a" and "b" are 5 and 3 
  // respectively, the result is 8.

  cout << "\n************ Important Note: Scope of Variables ************ " << endl;
  cout << "The scope of variables declared within a function or any other inner block is only their own function or their own block and cannot be used outside of them. For example, in the previous example it would have been impossible to use the variables a, b or r directly in function main since they were variables local to function addition. Also, it would have been impossible to use the variable z directly within function addition, since this was a variable local to the function main. " << endl;
  cout << "\n************************************************************* " << endl;



 cout << "\n Program termination "<< endl;
  return 0;
   
} //end of: int main() {
