// for_loop.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/control/

// Tell the preprocessor to load the iostream file
#include <iostream>
// Tell the preprocessor to load the stringstream file
#include <sstream>
// Tell the preprocessor to load the string file
#include <string>

// Load standard C++ libraries
using namespace std;

// main function declaration
int main () {

  cout << "The for loop: Exaple" << endl;
  cout << "********************" << endl;

  // The "for" loop format is: 
  // for (initialization; condition; increase) statement;

  // d its main function is to repeat statement while condition remains true, 
  // like the while loop. But in addition, the for loop provides specific 
  // locations to contain an initialization and an increase statement. 
  // So this loop is specially designed to perform a repetitive action with a 
  // counter which is initialized and increased on each iteration.
  //  It works in the following way:
  // 1. initialization is executed. Generally it is an initial value setting 
  // for a counter variable. This is executed only once.
  // 2. condition is checked. If it is true the loop continues, otherwise the 
  // loop ends and statement is skipped (not executed).
  // 3. statement is executed. As usual, it can be either a single statement 
  // or a block enclosed in braces { }.
  // 4. finally, whatever is specified in the increase field is executed and the loop gets back to step 2.


  string myString;
  int myInt;
  string anotherString;
  int remainder;
  
  cout << "\nPlease enter a number: " ;
  getline(cin,myString);
  stringstream(myString) >> myInt;

  for( int i=1 ; i<=myInt; i++) {
  
    if ( i%2 == 0) {
      cout << "Number " << i << " is EVEN and divided by 2 gives: " << i/2 << "." << endl;  
    }
    else {
      cout << "Number " << i << " is ODD and divided by 2 gives: " << i/2 << " + 1/2." << endl;
    }

  }

  // Remarks: The initialization and increase fields are OPTIONAL. They can 
  // remain empty, but in all cases the semicolon signs between them must be 
  // written. For example we could write: 
  // for ( ; n < 10; ) 
  // if we wanted to specify no initialization and no increase; or 
  // for ( ; n<10 ; n++) if we wanted to include an increase field but 
  // no initialization (maybe because the variable was already initialized 
  // before).
	  
  cout << "\nOptionally, using the comma operator (,) we can specify more than one expression in any of the fields included in a for loop, like in initialization, for example. The comma operator (,) is an expression separator, it serves to separate more than one expression where only one is generally expected. For example, suppose that we wanted to initialize more than one variable in our loop: " << endl;
  
  cout << "\nfor ( int i = 79 , int j = 100; i!=j; j--) {" << endl;
  cout << "\t cout << j << \", \" ; " << endl;
  cout << "}\n" ;

  int i,j;
  for ( i = 79 , j = 100; i!=j; j--) {
    cout << j << ", " ;
  }

  cout << "\n*********************************";
  cout << "\nfor ( int i = 0 , int j = 10; i!=j; i++, j--) {" << endl;
  cout << "\t cout << i << j << \", \" ; " << endl;
  cout << "}\n" ;

  for ( i = 0 , j = 10; i!=j; i++, j--) {
    cout << " i = " << i << ", j = " << j << ", " ;
  }

  cout << "FIRE!\n";

  cout << "\n*Program termination*" << endl;
  // program termination
  return 0;
  
} //end of: int main () {
