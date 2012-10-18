// multi_dimensional_arrays.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/arrays/

// Tell the preprocessor to include the iostream file
#include <iostream>

#include <string>

// Load standard C++ libraries
using namespace std;

// Define some constants
#define COLUMNS 5 // i.e. the array WIDTH
#define ROWS 3    // i.e. the array HEIGHT

// prototype function declaration
void instructions(void);
void multidimensionalArray(void);
void pseudoMultidimensionalArray(void);

// main function declaration
int main() {
  
  cout << "************************" << endl;
  cout << "\nMulti-dimensional arrays" << endl;
  cout << "************************" << endl;

  // call the function instructions
  instructions();

  cout << "\n multidimensionalArray()" << endl;
  cout << "************************" << endl;

  // call the function multidimensionalArray
  multidimensionalArray();
  
  cout << "\n pseudoMultidimensionalArray()" << endl;
  cout << "******************************" << endl;

  // call the function pseudoM!ultidimensionalArray
  pseudoMultidimensionalArray();
  
  cout <<"\nProgram Termination!" << endl;
  return 0;

} //end of: int main() {


// auxiliary functions here

void instructions(void) {

  cout << "\nInstructions" << endl;
  cout << "************" << endl;

  cout << "\n Multidimensional arrays can be described as \"arrays of arrays\". For example, a bidimensional array can be imagined as a bidimensional table made of elements, all of them of a same uniform data type. For example, a 2d array carrying integers is declared by:" << endl;

  cout << "int my2dArray[10][10]; " << endl;

  cout << "\n The multi-dimensional array \"my2dArray\" represents a bi-dimensional array of 10 per 10 elements of type \"int\". The way to reference the second element vertically and fourth horizontally in an expression would be: \n my2dArray[1][3]. " << endl;

  cout << "\nMore generically, to reference the \"nth\" vertical and \"mth\" horizontal element of a 2d array you type: \n my2dArray[n-1][m-1]; " << endl;
  
  cout << "\n \n Multidimensional arrays are not limited to two indices (i.e., two dimensions). They can contain as many indices as needed. But be careful! The amount of memory needed for an array rapidly increases with each dimension. For example: \n char century[100][346][24][60][60]; \n declares an array with a \"char\" element for each second in a century, which is more than 3 billion \"chars\"!!! So this declaration would consume more than 3GB of memory (remember, size of 1 \"char\"!!! is 1byte)." << endl;

  cout << "\n Multidimensional arrays are just an abstraction for programmers, since we can obtain the SAME results with a simple array just by putting a factor between its indices: \n int exampleArray[3][5]; // is equivalent to \n int exampleArray[15]   // (3*5=15) "<< endl;

} // end of: void instructions(void) {

void multidimensionalArray(void) {

  int my2dArray[ROWS][COLUMNS];
  int n;
  int m;

  for (n = 0; n < ROWS; n++){
   for (m = 0; m < COLUMNS; m++){
     my2dArray[n][m]=(n+1)*(m+1);
    }
 }
 for (n=0;n<ROWS;n++) {
   for (m=0;m<COLUMNS;m++){
     cout << my2dArray[n][m] << " " ;
   }
   cout << "\n" << endl; 
 }
} //end of: void multidimensionalArray() {

void pseudoMultidimensionalArray(void) {

  int my2dPseudoArray[ROWS*COLUMNS];
  int n,m;

  for (n=0; n < ROWS; n++) {

    for (m=0; m < COLUMNS; m++) {
      my2dPseudoArray[n*COLUMNS+m] = (n+1)*(m+1);

    } //end of:     for (m=0; m < COLUMNS; m++) {
    
  } //end of: for (n=0; n < ROWS; n++) {

  for( n=0; n < ROWS*COLUMNS; n++) {
    cout << my2dPseudoArray[n] << " " ;
    }
    cout << "\n" << endl;

    // or, can print array out like 2d:
    string changeLine = "\n\n";
    string doNothing = "";
      
  for( n=0; n < ROWS*COLUMNS; n++) {
    cout << ( n%5 == 0 ? changeLine : doNothing ) ;
    cout << my2dPseudoArray[n] << " " ;
    
  }
    cout << "\n" << endl;


    
} //end of: void multidimensionalArray() {



// void arrayExample(void) {
  
//   int my2dArray[5][5];
  
//   for( int i = 0; i < 5; i++) {
    
//     my2dArray[i][]= 1; // fill in the columns with the number 1

//   }

//   for( int j = 0; j < 5; j++) {
    
//     my2dArray[][j]= 0; // fill in the columns with the number 1

//   }


// } //end of: void arrayExample(void) {
