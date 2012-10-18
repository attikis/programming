// input_output.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/basic_io/

// Tell the preprocessor to include the iostream
# include <iostream>

// Load standard C++ libraries
using namespace std;


// main function declaration
int main () {


  cout << "\nStandard Output (cout) " << endl;
  cout << "***********************" << endl;
  // Standard Output (cout)
  // By default, the standard output of a program is the screen, and the C++ 
  // stream object defined to access it is "cout".
  // "cout" is used in conjunction with the insertion operator "<<"
  
  cout << "Output" << endl; // prints: Output 
  cout << 120 << endl; // prints: 120
  int x = 100;
  cout << x << endl; // prints: value of x 
  
  // The insertion operator "<<" can be used more than once in a statement"
  cout << "The value of x is " << x << endl; 
  
  // *********************************************************************
  cout << "\nStandard Input (cin) " << endl;
  cout << "***********************" << endl;

  // Standard Input (cin).
  // The standard input device is usually the keyboard. Handling the standard 
  // input in C++ is done by applying the overloaded operator of extraction 
  // ">>" on the cin stream. The operator must be followed by the variable 
  // that will store the data that is going to be extracted from the stream. 
  // For example:
  
  int age;  
  string teenFalse = "not";
  string teenTrue = "still";
  string YorN;
  string knows = "Good! You are more mature than I thought !";
  string notKnows = "Well, it is time somebody told you !";
  int trials = 0;
  
  cout << "Please enter your age: " ;
  cin >> age ;
  
  cout << "\nYou DO know that you are " << ( (age >= 20 ) || ( age < 13) ? teenFalse : teenTrue ) << " a teenager, right? \n Answer \"y\" or \"n\" : " ;
  cin >> YorN;
  
  if ( ( YorN == "y" ) || ( YorN == "n") ){
      
      cout << ( (YorN == "y" ) ? knows : notKnows ) << endl;
}
  else {  
    while( !( ( YorN == "y" ) || ( YorN == "n") ) ) {
      
      trials ++;
      cout << "I said answer with \"y\" or \"n\" dumbass !!" << endl;
      cin >> YorN;
      
      if( ( YorN == "y" ) || ( YorN == "n") ){
	
	cout << ( (YorN == "y" ) ? knows : notKnows ) << endl;
      }
      if (trials == 5){ 
	cout << "\n Oh, grow up, will you? " <<endl;
	break;
      }
    }
  }
  
  cout << "\n" << endl;
  // program termination
  return 0;
  
} //end of: int main () {
