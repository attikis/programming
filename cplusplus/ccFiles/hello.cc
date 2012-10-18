// hello.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/program_structure/
Note: Comments Precede the command-lines


// Tell the preprocessor to include the iostream standard file, which includes 
// all the declaration of the basis standard input-output library in C++
#include <iostream>

// All the elements of the standard C++ library are declared within what is called 
// a namespace, the namespace with the name "std". To access its functionality 
// we declare with the following expression that we will be using these entities.
using namespace std;

// The main function is the point by where all C++ programs start their execution, 
// independently of its location within the source code. It does not matter whether
// there are other functions with other names defined before or after it.
int main () // function declaration. declared with ()
{ //the body of the main function is enclosed in braces 
 
  cout << "Hello World!" << endl;
  
//The "return" statement causes the main function to finish. 
// return may be followed by a return code (here 0). A return code of 0 for the 
// main function is generally interpreted as the program worked as expected without 
// any errors during its execution. 
return 0;
}
