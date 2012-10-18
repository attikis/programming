// my_multi_dimensional_arrays.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/arrays/

// Tell the preprocessor to include iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;

// my definitions here
#define ROWS 8
#define COLUMNS 8

// prototype function declaration
void arrayExample(void);

// main function declaration
int main() {

  arrayExample();
  
  cout << "\n Program Termination! "<< endl;
  return 0;
  
} //end of: int main() {

// auxiliary functions here
void arrayExample(void) {

  int diagonalMatrix[ROWS][COLUMNS];
  
  for( int i =0; i < ROWS; i++){
    
    for( int j =0; j < COLUMNS; j++){

      diagonalMatrix[i][j] =  (i==j) ? 1 : 0;

    } //end of:     for( int j =0; j < COLUMNS; j++){

  } //end of:   for( int i =0; i < ROWS; i++){

  cout << "\n" << endl;

  for( int i =0; i < ROWS; i++){
    
    for( int j =0; j < COLUMNS; j++){

      cout << " " << diagonalMatrix[i][j] ;

    } //end of:     for( int j =0; j < COLUMNS; j++){

    cout << "\n" << endl;
    
  } //end of:   for( int i =0; i < ROWS; i++){

  
}  //end of: void arrayExample(void) {
