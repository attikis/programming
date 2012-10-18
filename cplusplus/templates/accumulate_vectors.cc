// vectors.cc

// Tell the preprocessor to include iostream
#include <iostream>
#include <vector>
#include <functional>
#include <numeric>

using namespace std;

// forward function declaration
vector<int> createVector(void);

// main function declaration 
  int main() {

    // create a vector of 10 ints, each initialised to the integer value "2".
    vector<int> testVector = createVector();
    
    // Use the accumulate function (not necessarily used with vectors! This is just an example)
    const float sum = accumulate(testVector.begin(), testVector.end(), 0.0);
    std::cout << "sum = " << sum << std::endl;


    cout << "\n Program Termination! " << endl;
    return 0;
    
  } //end of: int main() {

vector<int> createVector(void){

  // declare vector
  vector<int> myIntVector(10, 2); // declare a vector capable of storing 10 integers, each of which is initialized to the value of 2
  
  // create vector iterator
  vector<int>::iterator it;
  
  cout << "myIntVector contains:" << endl;
  
  for ( it=myIntVector.begin() ; it < myIntVector.end(); it++ )
    cout << " " << (*it) << endl;

  cout << endl;

  return myIntVector;

} //eof: createVector(void)
