// functionsIIa.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/functions2/

// Tell the preprocessor to load the file iostream
#include <iostream>
// Tell the preprocessor to load the file string 
#include <string>
// Tell the preprocessor to load the file stringstream
#include <sstream>

// Load standard C++ libraries
using namespace std;

// Until now, in all the functions we have seen, the arguments passed to the
// functions have been passed "by value". This means that when calling a 
// function with parameters, what we have passed to the function were COPIES 
// of their values but never the variables themselves. For example, suppose that we called our first function addition using the following code:
// int x=5, y=3, z;
// z=addition( x , y);
// What we did in this case was to call to function addition, passing the 
// values of x and y, i.e. 5 and 3 respectively, but not the variables x 
// and y themselves.
// This way, when the function "addition" is called, the value of its LOCAL 
// variables "a" and "b" become 5 and 3 respectively, but any modification to 
// either "a" or "b" within the function addition will NOT have any effect in 
// the values of x and y outside it, because variables x and y were not 
// themselves passed to the function. Instead, only copies of their values at 
// the moment the function was called.

// But there might be some cases where you need to manipulate from inside a 
// function the value of an external variable. 
// For that purpose we can use arguments passed "by reference", as in the 
// function duplicate of the following example:

// declare a void type function. 
void duplicate( int& a, int& b, int& c){
//It takes 3 integers as parameters passed "by reference"!

  a*=2; // same as a = a*2;
  b*=2;
  c*=2;
  
}// end of: void duplicate( int& a, int& b, int& c){

// another function
void convertEvenToOdd(int& a) {
  // The ampersand sign (&) is what specifies that the corresponding arguments
  // of the function are to be passed "by reference" instead of "by value".

  cout << "\n*This function will check if the number passed to it is Even or Odd. If Odd it will convert to the nearest Even integer (incease)." << endl;
  bool isEven = 1;
  bool isOdd = 0;
  
  switch(a%2) {
  case 0: 
    cout << "**The number you have entered is even. Nothing will be done. Exiting function..." << endl;
  break;
 default:
   a = a+1;
   if ( (a%2 == 0) ? isEven : isOdd ) // conditional statement
   if(isEven) cout << "**The number you have entered is NOT even! The new number is " << a << endl;
   else { break;}
     
  } //end of:   switch(a%2) {
     

}  // end of: void convertEveToOdd(int a&) {

// main function declaration
int main() {

  int x=1, y=3, z=7;
  
  cout << "\nThe original values of x, y, z are: x = " << x << " , y = " << y << " , z = " << z << endl;
  
  // call the duplicate function. This will will return 2*x, 2*y, 2*z
  duplicate( x, y, z);
  
  cout << "The new values of x, y, z are: x = " << x << " , y = " << y << " , z = " << z << endl;

  cout << "From now on these are the values of x, y, z. This is because the variables x, y, z were not passed \"by value\" but instead \"by reference\" !!! " << endl;
  
  string myString;
  int myNum;
  
  cout << "\nEnter any number: ";
  getline(cin , myString);
  stringstream(myString) >> myNum;
  convertEvenToOdd(myNum);

  cout << "\n***Summary: When a variable is passed by reference we are not passing a copy of its value, but we are somehow passing the variable itself to the function and any modification that we do to the local variables will have an effect in their counterpart variables passed as arguments in the call to the function. " << endl;
  cout << "\nProgram termination." << endl;

} //end of: int main() {
