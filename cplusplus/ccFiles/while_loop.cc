// while_loop.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/control/

// Tell the preprocessor to load the iostream
#include <iostream>
// Tell the preprocessor to include the file sting
#include <string>
// Tell the preprocessor to include the file stringstream
#include <sstream>
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

  string myString;
  int counter = 0;
  int CountDown = 0;
  int CountUp = 0;
  cout << "\nwhile loop: CountDown and CountUp example" << endl;
  cout << "*******************************************" << endl;

  cout << "Enter the starting number for CountDown : " ;
  getline(cin,myString); //input 
  stringstream(myString) >> CountDown;
  
  while ( CountDown > 0 ) {
    cout << CountDown << ", " ;
    --CountDown;
  }
  cout << "FIRE!" << endl;
  
  cout << "\nEnter the starting number for CountUp : " ;
  getline(cin,myString); //input 
  stringstream(myString) >> CountUp;

  while ( counter <= CountUp ) {
    cout << counter << ", " ;
    ++counter;
  }
  cout << "FIRE!" << endl;

  //  When creating a while-loop, we must always consider that it has to end 
  // at some point, therefore we must provide within the block some method to
  // force the condition to become false at some point, otherwise the loop 
  // will continue looping forever. In this case we have included --n; 
  // that decreases the value of the variable that is being evaluated in the 
  // condition (n) by one - this will eventually make the condition (n>0) 
  // to become false after a certain number of loop iterations: 
  // to be more specific, when n becomes 0, that is where our while-loop and 
  // our countdown end.

  cout << "\n * Program termination *" <<endl;
  // program termination
  return 0;




} //end of: int main () {

