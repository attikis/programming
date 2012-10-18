// if_and_else.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/control/

// Tell the preprocessor to load input-output ostream (iostream)
#include <iostream>
// Include stringstream library
#include <sstream>
// Include string library
#include <string>

// Load standard C++ libraries
using namespace std;

// Conditional structure: if and else
// The "if" keyword is used to execute a statement or block only if a 
// condition is fulfilled. Its form is: if (condition) statement
// Where condition is the expression that is being evaluated. If this 
// condition is true, statement is executed. If it is false, statement is 
// ignored (not executed) and the program continues right after this 
// conditional structure.
// We can additionally specify what we want to happen if the condition is not 
// fulfilled by using the keyword "else": 
// if (condition) statement1 else statement2

// main function declaration
int main() {

  string myString;
  int day;
  int month;
  int year;
  int age;
  
//   cout << "\nWhat day where you born? (from 1 to 31)" << endl;
//   getline(cin,myString); // input 
//   stringstream(myString) >> day; // stream "myString" to "day" variable

//   cout << "\nWhat month? (from 1 to 12)" << endl;
//   getline(cin,myString); // input 
//   stringstream(myString) >> month; // steam "myString" to "month" variable

  cout << "\nWhat year? (Example: 1953)" << endl;
  getline(cin,myString); // input
  stringstream(myString) >> year; // steam "myString" to "year" variable
  cout << "\n year: " << year << endl;
  age = 2009 - year;
  cout << "\n age: " << age << endl;
  
  if( ( age < 18 ) && ( age >=0 ) )
    cout << "\nOkay, that makes you "<< age << " years old. I am sorry but you are too young to have sex. Try again in a few years..." << endl;
  else if ( age == 18)
    cout << "\nOkay, that makes you "<< age << " years old. You are legally eligible to have sex..." << endl;
  else if( ( age > 18 ) && ( age < 50 ) )
    cout << "\nOkay, that makes you "<< age << " years old. Keep on rocking in the free world ..." << endl;
    else if ( ( age > 50 ) && ( age < 150 ) )
      cout << "\nOkay, that makes you "<< age << " years old. Aren't you too old for this shit ???" << endl;
    else 
      cout << "\n WTF dude? How hard can it be to enter a year correctly? " << endl;
  // program termination
  return 0;
  
} //end of: int main () {
