// stringstream.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/basic_io/

// Tell the preprocessor to load the file iostream
#include <iostream>
// Tell the preprocessor to load the string class
#include <string>
// Tell the preprocessor to load the stringstream class
#include <sstream>
using namespace std;

// main function declaration
int main() {

// stringstream
// The standard header file <sstream> defines a class called "stringstream"
// that allows a string-based object to be treated as a stream. This way we 
// can perform extraction ( >> )or insertion operations ( << ) from/to strings,
// which is especially useful to convert strings to numerical values and vice 
// versa. 
// For example, if we want to extract an integer from a string we can write:

  string myString = "1204";  // same as:  string myString ("1204");
  int myInt;
  stringstream(myString) >> myInt;
  cout << myInt << endl;
  // This declares a string object with a value of "1204", and an int object. 
  // Then we use stringstream's constructor to construct an object of this 
  // type from the string object. Because we can use stringstream objects as 
  // if they were streams, we can extract an integer from it as we would have 
  // done on "cin" by applying the extractor operator (>>) on it followed 
  // by a variable of type int.

  cout << "\n Example" << endl;
  cout << " ********" << endl;
  
    string anotherString;
    float price = 0;
    int quantity = 0;
    
    cout << "Enter price: ";
    getline (cin,anotherString); // input by keyboard a value for anotherString
    stringstream(anotherString) >> price; // put input value to "price"
    cout << "Enter quantity: ";
    getline (cin,anotherString); // input by keyboard a value for anotherString
    stringstream(anotherString) >> quantity; // put input value to "quantity"
    cout << "price: " << price << quantity << endl;
    cout << "quantity: " << quantity << endl;
    cout << "anotherString : " << anotherString << endl;
    cout << "Total price: " << price*quantity << endl;

    cout << "\n In this example, we acquire numeric values from the standard input indirectly. Instead of extracting numeric values directly from the standard input, we get lines from the standard input (cin) into a string object (anotherString), and then we extract the integer values from this string into a variable of type int (quantity). \n Using this method, instead of direct extractions of integer values, we have more control over what happens with the input of numeric values from the user, since we are separating the process of obtaining input from the user (we now simply ask for lines) with the interpretation of that input. Therefore, this method is usually preferred to get numerical values from the user in all programs that are intensive in user input. " << endl;
    
    cout << "\n Summary: Then why not use just \"cin\" instead? Because it is easier using \"stringstream\". For example, to input 5 values using \"cin\" the programmer would have to write:" << endl;
    cout << "\n \"cin >> a >> b >> c >> d >> e >> endl; "<< endl;\
    cout << "\n Well that is not efficient is it? Imagine if you had to input 100 variables. Then you would have to declare 100 variables and then input them by keyboard pressing ENTER for each input!! Stringstreams do make life easier !" << endl;

    
    cout << "\n" << endl;
    // program termination
    return 0;
    
} //end of: int main() {

  
