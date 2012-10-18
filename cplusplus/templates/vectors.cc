// vectors.cc

// Tell the preprocessor to include iostream
#include <iostream>
#include <vector>

using namespace std;

// forward function declaration
void defaultVector(void);
void myIntVector(void);
void myStringVector(void);

// main function declaration 
  int main() {
    
    //    defaultVector();
    //    myIntVector();
    myStringVector();
    
    cout << "\n Program Termination! " << endl;
    return 0;
    
  } //end of: int main() {

void defaultVector(void){

  // declare vector
  vector<int> myVector(10); // declare a vector capable of storing 10 integers, each of which is initialized to the default value of ints
  
  // create vector iterator
  vector<int>::iterator it;
  
  cout << "myVector contains:" << endl;
  
  for ( it=myVector.begin() ; it < myVector.end(); it++ )
    cout << " " << (*it) << endl;

  cout << endl;

} //end of void defaultVector(void){


void myIntVector(void){

  // declare vector
  vector<int> myIntVector(10, 99); // declare a vector capable of storing 10 integers, each of which is initialized to the value of 99
  
  // create vector iterator
  vector<int>::iterator it;
  
  cout << "myIntVector contains:" << endl;
  
  for ( it=myIntVector.begin() ; it < myIntVector.end(); it++ )
    cout << " " << (*it) << endl;

  cout << endl;

} //end of void myIntVector(void){


void myStringVector(void){

  // declare vector
  //vector<string> myStringVector(10, ""); // declare a vector capable of storing 10 integers, each of which is initialized to the value of 99
  vector<string> myStringVector; // declare a vector capable of storing 10 integers, each of which is initialized to the value of 99
  
  // create vector iterator
  vector<string>::iterator it;
  
  cout << "myStringVector contains:" << endl;
  //  cout << "size = " << myStringVector.size();
  
  myStringVector.push_back(" tau-jet ");   
  myStringVector.push_back(" b-jet ");   
  myStringVector.push_back(" bbar-jet ");   
  myStringVector.push_back(" q-jet ");   
  myStringVector.push_back(" qbar-jet ");   
  
  // How to cout a vector element
  cout << myStringVector[1] << endl;
  cout << myStringVector[1] << endl;
  cout << myStringVector[1] << endl;
  cout << "\n\n"<< endl;

  for ( it=myStringVector.begin() ; it < myStringVector.end(); it++ ){ 
    cout << " " << (*it) << endl;
    }

} //end of void myStringVector(void){
