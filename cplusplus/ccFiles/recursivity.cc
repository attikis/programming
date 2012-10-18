// recursivity.cc
// C++ Tutorial:  http://cplusplus.com/doc/tutorial/functions2/

// Tell the preprocessor to load the file iostream
#include <iostream>
// Tell the preprocessor to include stringstream
#include <sstream>
// Tell the preprocessor to include sting
#include <string>

// Load standard C++ libraries
using namespace std;

void instructions (void) {

  cout <<"\nRecursivity" << endl;
  cout <<"************\n" << endl;
  
  cout << "* Recursivity is the property that functions have to be called by THEMSELVES. It is useful for many tasks, like sorting or calculating the factorial of numbers. For example, to obtain the factorial of a number (n!) the mathematical formula would be:" << endl;
  cout << "n! = n * (n-1) * (n-2) * (n-3) ... * 1 "<< endl;
  cout << "More concretely, 5! (factorial of 5) would be: "<< endl;
  cout << " 5! = 5 * 4 * 3 * 2 * 1 = 120 \n" << endl;
  
} //end of: void instructions (void) {

float factorial( float a ) { 
  
  // N.B: This function has a limitation because of the data type we used in its design 
  // (float) for more simplicity. The results given will not be valid for values much 
  // greater than 10! or 15!, depending on the system you compile it.
  
  if ( a > 1) {

    cout << a << "x";

    return ( a*factorial(a-1) );
  }
  else{ 
    cout << "1 = " ;
    return(1); // if a = 0 return the value "1"
    
  } 
    
} // end of: float factorial(float& a) {


  // main function declaration 
int main () {
  
  instructions();
  
  string myString;
  float myNumber;
  
  cout << "** This program calculates the factorial (!) of a number..." << endl;
  cout << "*** Please type a number: ";
  getline(cin,myString);
  stringstream(myString) >> myNumber;
  
  cout << "\n" << myNumber << "! = ";
  cout << factorial(myNumber) << endl;
  
  cout << "\n**** Program Termination!" << endl;
  return 0;
  
}  // end of: int main() {

