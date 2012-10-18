// do_while_loop.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/control/

// Tell the preprocessor to load the iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;

// main function declaration
int main () {

  // Iteration structures (loops)
  // Loops have as purpose to repeat a statement a certain number of times 
  // or while a condition is fulfilled. The while loop format is:
  // while (expression) statement
  // and its functionality is simply to repeat statement while the condition 
  // set in the expression is true.
  // The do-while loop has format of form:
  // do statement while (condition);
  // Its functionality is exactly the same as the while loop, except that 
  // condition in the do-while loop is evaluated AFTER the execution of 
  // statement instead of before, granting at LEAST ONE execution of statement
  // even if condition is never fulfilled. 
  // For example, the following example program echoes any number you enter 
  // until you enter 0.

  cout << "\n do-while loop: Example" << endl;
  cout << "*************************" << endl;

  unsigned long n; 
  
  do{
  cout << "Enter the starting number (Press 0 to exit): " ;
  cin  >> n;
  cout << "You entered: " << n << "\n" << endl;
  } while (n!=0);

  cout << "\n Some Remarks: The do-while loop is usually used when the  condition that has to determine the end of the loop is determined within the loop statement itself, like in the previous case, where the user input within the block is what is used to determine if the loop has to end. In fact if you never enter the value 0 in the previous example you can be prompted for more numbers forever... " << endl;

  cout << "\n * Program termination *" <<endl;
  // program termination
  return 0;




} //end of: int main () {

