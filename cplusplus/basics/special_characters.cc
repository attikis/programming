// special_characters.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/constants

// In addition to decimal numbers (those that we use every day) C++ allows the
// use as literal constants of octal numbers (base 8) and hexadecimal numbers 
// (base 16). If we want to express an octal number we have to PRECEDE it with
// a 0 (zero character). And in order to express a hexadecimal number we have 
// to precede it with the characters 0x (zero, x). For example, the following 
// literal constants are all equivalent to each other:
// 75         // decimal
// 0113       // octal
// 0x4b       // hexadecimal 
// All of these represent the same number: 75 (seventy-five) expressed as a 
// base-10 numeral, octal numeral and hexadecimal numeral, respectively.

// Character and string literals have certain peculiarities, like the escape 
// codes. These are special characters that are difficult to express otherwise 
// in the source code of a program, like newline (\n) or tab (\t). 
// All of them are preceded by a backslash (\). Here you have a list of some:
//  \n   newline
//  \r   carriage return
//  \t   tab
//  \v   vertical tab
//  \b   backspace
//  \f   form feed (page feed)
//  \a   alert (beep)
//  \'   single quote (')
//  \"   double quote (")
//  \?   question mark (?)
//  \\   \backslash (\)

// Tell the preprocessor to include the iostream standard file
#include <iostream>

// Load standard C++ libraries
using namespace std;

int main() {

  string myString = "This is an example of how to use special charactes !";
  string anotherString = "More info can be found at:  http://cplusplus.com/doc/tutorial/constants";
    
  cout << "\f" << myString << "\n" << anotherString << " \f "<< endl;

  cout << "This is an example of how to include \'single quotation marks\' and \"double quotation marks\"." << endl;

  // Finally, if we want the string literal to be explicitly made of wide 
  // characters (wchar_t), instead of narrow characters (char), we can 
  // precede the constant with the L prefix:
  cout << "\n I am an encoded text message" << endl;
  cout << L"\n I am an encoded text message" << endl;
  

// program termination
 return 0;
    
  } // end of: int main() {
