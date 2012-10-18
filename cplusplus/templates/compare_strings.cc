// compare_strings.cc
// see: http://www.cplusplus.com/reference/string/string/compare/

// Tell the preprocessor to include the standard file iostream
#include <iostream>
#include <string>

// Load standard C++ libraries
using namespace std;


// Compare strings
// ***************
// Compares the content of this object (or a substring of it, known as compared (sub)string) to the content of a comparing string, which is formed according to the arguments passed.
// The member function returns 0 if all the characters in the compared contents compare equal, a negative value if the first character that does not match compares to less in the object than in the comparing string, and a positive value in the opposite case.
// Notice that for string objects, the result of a character comparison depends only on its character code (i.e., its ASCII code), so the result has some limited alphabetical or numerical ordering meaning.

//For other basic_string class instantitations, the comparison depends on the specific traits::compare function, where traits is one of the class template parameters.

// main function declaration

int main() {

  string a ("alex");
  string b ("alex");
  string c ("blex");
  cout << " a.compare(b) = !" << a.compare(b) << endl; //returns 0 because all the characters in the compared contents equal

  cout << " a.compare(c) = " << a.compare(c) << endl; // returns a -ve value because the 1st character that does not match compares to less in the object than in the comparting string

  cout << " c.compare(a) = " << c.compare(a) << endl; // returns a +ve value because the 1st character that does not match compares to less in the object than in the comparting string
  


  cout << "\n" << endl;
  // program termination 
  return 0;

} //end of: int main () { 
