// break_continue_goto_exit.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/control/

// Tell the preprocessor to include the iostream
#include <iostream>
// Load standard C++ libraries
using namespace std;

// main function declaration
int main() {

  cout << "The break statement " << endl;
  cout << "******************* " << endl;
  
  // The break statement
  // Using "break" we can leave a loop even if the condition for its end is 
  // not fulfilled. It can be used to end an infinite loop, or to force it to 
  // end before its natural end. 
  // For example, we are going to stop the count down before its natural end (maybe because of an engine check failure?):

  int n;

  for ( n=10; n>0; n--){
    cout << n << ", " << endl;
      
      if ( n==3){
	cout << "Countdown aborted!" << endl;
	break;
      } //end of:       if ( n==3){ 

  } //end of:   for ( n=10; n>0; n--){
  


  cout << "\nThe continue statement " << endl;
  cout << "********************** " << endl;
  
  // The continue statement causes the program to skip the rest of the loop 
  // in the current iteration as if the end of the statement block had been 
  // reached, causing it to jump to the start of the following iteration. 
  // For example, we are going to skip the number 5 in our countdown:
  for (n=10; n>0; n--){
    if(n==5){continue;}
    cout << n << ", " << endl; // N.B.: AFTER the "if" condition !
} //end of:   for (n=10; n>0; n--){

  cout << "\nThe goto statement " << endl;
  cout << "********************** " << endl;
  
  // The goto statement allows to make an absolute jump to another point in 
  // the program. You should use this feature with caution since its 
  // execution causes an unconditional jump ignoring any type of nesting 
  // limitations.
  // The destination point is identified by a label, which is then used as an 
  // argument for the goto statement. A label is made of a valid identifier 
  // followed by a colon (:).  
  // Generally speaking, this instruction has no concrete use in structured 
  // or object oriented programming aside from those that low-level 
  // programming fans may find for it. For example, here is our 
  // countdown loop using goto:
  
  int k=10;
  
 loop:
  cout << k << ", " ;
  k--;
  if(k>0) goto loop;

  cout << "\nThe exit statement " << endl;
  cout << "******************** " << endl;
  
  // exit is a function defined in the cstdlib library.
  // The purpose of exit is to terminate the current program with a 
  // specific exit code. Its prototype is:
  // void exit (int exitcode);
  // The exitcode is used by some operating systems and may be used by 
  // calling programs. By convention, an exit code of 0 means that the 
  // program finished normally and any other value means that some error or
  // unexpected results happened.
  
  // Example:  exit(1);
  
  cout << "\nProgram termination" << endl;
  return 0;

} // end of: int main {
