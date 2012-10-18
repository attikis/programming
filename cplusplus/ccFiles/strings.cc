// strings.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/variables/

// Tell the preprocessor to include the iostream standard file
#include <iostream>

// Use the standard C++ library
using namespace std;

// main function declaration
int main() {

  string myString = "I am a string";
  // string myString = ("I am a string");   // this is also acceptable
  
  cout << myString << endl;

  // As any other data type, stings can also be declared without any initial value
  // and being assigned values during execution
  string anotherString;
  anotherString = "This is the initial string content";
  cout << anotherString << endl;
  anotherString = "This is a different string content";
  cout << anotherString << endl;


} // end of: int main() {
