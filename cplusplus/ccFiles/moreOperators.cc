// moreOperators.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/operators/

// Tell preprocessor to load the file "iostream"
#include <iostream>

// Load standard C++ libraries
using namespace std;

// main function declaration
int main() {

  cout << "Comma operator ( , ) " << endl;
  cout << "*********************" << endl;
  // Comma operator ( , )
  // The comma operator (,) is used to separate two or more expressions 
  // that are included where only one expression is expected. When the set 
  // of expressions has to be evaluated for a value, only the rightmost 
  // expression is considered. For example, the following code:
  // a = (b=3, b+2);
  // Would first assign the value 3 to "b", and then assign b+2 
  // to variable "a". So, at the end, variable "a" would contain the value 5 
  // and variable "b" the value 3.
  int a;
  int b;
  cout << "1) Performing operation a = (b=1 , b-2) gives: " << (a = (b=1 , b-2) ) << endl;
  cout << "\nThe value of variable \"a\" is " << a << " and the value of variable \"b\" is "<< b << "\n" << endl;
  
  cout << "2) Performing operation a = (b=10 , b-1) gives: " << (a = (b=10 , b-1) ) << endl;
  cout << "\nThe value of variable \"a\" is " << a << " and the value of variable \"b\" is "<< b << "\n" << endl;
    
  // *************************************************************************
  cout << "Explicit type casting operator" << endl;
  cout << "******************************" << endl;
    
  // Explicit type casting operator
  // Type casting operators allow you to convert a variable of a given type 
  // to another. There are several ways to do this in C++. The simplest one 
  // is to precede the expression to be converted by the new type enclosed 
  // between parentheses (()):
  int i;
  float f = 3.14;
  i = (int) f;
  cout << "The value of i is " << i << endl;
  // The previous code converts the float number 3.14 to an integer value (3), 
  // the remainder is LOST. 
  
  // Another way to do the same thing is using the functional notation: 
  // preceding the expression to be converted by the type and enclosing the 
  // expression between parentheses:
  double d = 6.129;
  i = int (d);
  cout << "The value of i is " << i << endl;
  cout << "\n" << endl;  
  // *************************************************************************

  cout << "sizeof()"<< endl;
  cout << "********" << endl;

  // This operator accepts one parameter, which can be either a type or a 
  // variable itself and returns the size in "bytes" of that type or object:
  bool myBool = 1;
  char myChar = a;
  int myInt = 10;
  float myFloat = 2.234;
  double myDouble = 10.4;
  
  cout << "\n The size of a \"bool\" variable is : " << sizeof(myBool) << endl;
  cout << "\n The size of a \"char\" variable is : " << sizeof(myChar) << endl;
  cout << "\n The size of an \"int\" variable is : " << sizeof(myInt)  << endl; 
  cout << "\n The size of a \"float\" variable is : " << sizeof(myFloat) << endl;
  cout << "\n The size of a \"double\" variable is : " << sizeof(myDouble) << endl;
  
  // This will assign the value 1 to "myChar" because char is a one-byte type.
  // The value returned by sizeof is a constant, so it is always determined 
  // before program execution.




  cout << "\n" << endl;  
  // program termination
  return 0;

} //end of: int main() {
