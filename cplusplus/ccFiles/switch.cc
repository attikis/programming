// switch.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/control/

// Tell preprocessor to load iostream 
#include <iostream>
// Tell preprocessor to load stringstream
#include <sstream>
// Tell preprocessor to load string
#include <string>

// Load standard C++ libraries
using namespace std;

// main function declaration
int main () {
  
  // The selective structure: switch.
  // The syntax of the switch statement is a bit peculiar. Its objective is to 
  // check several possible constant values for an expression. Something 
  // similar to what we did at the beginning of this section with the 
  // concatenation of several if and else if instructions. 
  // Its form is the following:
  //switch (expression)
  //{
  //case constant1:
  //group of statements 1;
  // break;
  //case constant2:
  //group of statements 2;
  //break;
  //.
  //.
  //.
  //default:
  //default group of statements
  //} //end of; switch(expression){
  
  // It works in the following way: switch evaluates expression and checks if 
  // it is equivalent to constant1, if it is, it executes group of statements 
  // 1 until it finds the break statement. When it finds this break statement 
  // the program jumps to the END of the switch selective structure.
  
  // If expression was not equal to constant1 it will be checked against 
  // constant2. If it is equal to this, it will execute group of statements 2 
  // until a break keyword is found, and then will jump to the end of the 
  // switch selective structure.
  // Finally, if the value of expression did not match any of the previously 
  // specified constants (you can include as many case labels as values 
  // you want to check), the program will execute the statements included 
  // after the "default:" label, if it exists (since it is optional).
  // Both of the following code fragments have the same behavior:

  cout << "\nSwitch example" << endl;
  cout << "**************" << endl;

  int dayOfWeek;
  int monday    = 1;
  int tuesday   = 2;
  int wednesday = 3;
  int thursday  = 4;
  int friday    = 5;
  int saturday  = 6;
  int sunday    = 7;
  
  cout << "Please type what day it is (Choose 1-7 ): " ;
  cin >> dayOfWeek ;
  
  switch(dayOfWeek) {
  case 1:
    cout << "Monday's menu: Kebab with chips and pitta." << endl;
    break;
  case 2:
    cout << "Tuesday's menu: Fish and chips." << endl;
    break;
  case 3:
    cout << "Wednesday's menu: Kebab with chips and pitta." << endl;
    break;
  case 4:
    cout << "Thursday's menu: Pasta with salad." << endl;
  break;
  case 5:
    cout << "Friday's menu: Ceasar Salad." << endl;
  break;
  case 6:
    cout << "Saturday's menu: Chicken soup." << endl;
  break;
  case 7:
    cout << "Sunday's menu: Souvla (chicken, lamb, pork) with jagged potatoes." << endl;
    break;
  default: // else(...)
    cout << "\n**** Invalid number input. Exiting ... ****" << endl;
    
  } // end of: switch(dayOfWeek) {

  cout << "\nN.B.: The switch statement is a bit peculiar within the C++ language because it uses labels instead of blocks. This forces us to put break statements after the group of statements that we want to be executed for a specific condition. Otherwise the remainder statements -including those corresponding to other labels- will also be executed until the end of the switch selective block or a break statement is reached. Also notice that \"switch\" can only be used to compare an expression against constants. Therefore we cannot put variables as labels (for example case n: where n is a variable) or ranges (case (1..3):) because they are not valid C++ constants. " << endl;


  cout << "\nProgram termination" << endl;
  return 0;
  
}  //end of: int main () {
