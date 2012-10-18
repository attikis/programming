// getline.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/basic_io/
// see also: http://www.cplusplus.com/reference/iostream/istream/getline/

// "cin" and strings
// We can use "cin" to get strings with the extraction operator ">>" as we 
// do with fundamental data type variables:

// However, "cin" extraction stops reading as soon as if finds any blank space
// character, so in this case we will be able to get just one word for each 
// extraction. This behavior may or may not be what we want; for example if 
// we want to get a sentence from the user, this extraction operation would 
// not be useful.

// In order to get ENTIRE LINES, we can use the function "getline", which is 
// the more recommendable way to get user input with cin.

// Tell the preprocessor to load the iostream file
#include <iostream>

// Include library for strings
#include <string>

// Load standard C++ libraries
using namespace std;

// main function declaration
int main() {
  cout << "*******************************" << endl;
  cout << "This is a \"getline\" tutorial." << endl;
  cout << "*******************************" << endl;
  cout << "\n istream& getline (char* s, streamsize n ); " << endl;
  cout << "\n istream& getline (char* s, streamsize n, char delim ); "<< endl;

  //Parameters:
  // s : A pointer to an array of characters where the string is stored as a 
  // c-string.

  // n : Maximum number of characters to store. This is an integer value of type 
  // streamsize. If the function stops reading because this size is reached, the 
  // failbit internal flag is set.
  
  // delim : The delimiting character. The operation of extracting succesive 
  // characters is stopped when this character is read. This parameter is optional,
  // if not specified the function considers '\n' (a newline character) to be the 
  // delimiting character. 

  string myString;

  cout << "\n What's your name? " << endl;
  getline(cin, myString); //The input will be assigned to the string "myString"
  cout << "\n Hello " << myString << ".\n" << endl;
  
  cout << " What's your favourite team? " << endl;
  getline(cin, myString); // replaces the previous content of "myString"
  cout << "\nReally? I like "<< myString << " too !" << endl;

  cout << "\n" << endl;
  // program termination
  return 0;

} //end of: int main() {
