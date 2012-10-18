// arrays_as_parameters.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/arrays/

// Tell the preprocessor to include iostream:
#include <iostream>

// Load standard C++ libraries:
using namespace std;

// definitions:
// #define LENGTH 8

// prototype function declaration:
void instructions(void);
void print1dArray(int myArray[], int length);
void print2dArray(int myArray[][10], int rows) ;


// main function declaration:
int main() {
  
  cout << "\n**********************************" << endl;
  cout << "Arrays as parameters to functions" << endl;
  cout << "**********************************\n" << endl;

  instructions();

  int first1dArray[ ] = {1, 2, 3, 5, 8, 13, 21, 34};
  int second1dArray[ ] = { 1, 3, 5, 7, 11, 13, 17};

  int first2dArray[8][10];  // N.B: columns must be 10, but rows can be anything
  
  for(int i=0; i<8; i++){ // row-handling
    for(int j=0; j<10; j++){ // column-handling
      
      first2dArray[i][j] = ( (i+j)%2==0 ) ? 1:0;

    }
  }

  print1dArray(first1dArray,8);
  print1dArray(second1dArray,7);
  
  print2dArray(first2dArray, 8);

  cout << "\n Program Termination!" << endl;
  return 0;  

} //end of: int main() {

// auxiliary functions here
void instructions(void) {

  cout << "At some moment we may need to pass an array to a function as a parameter. In C++ it is NOT possible to pass a complete block of memory \"by value\" as a parameter to a function, but we ARE allowed to pass its address. In practice this has almost the same effect and it is a much faster and more efficient operation. In order to accept arrays as parameters the only thing that we have to do when declaring the function is to specify in its parameters the \"element type\" of the array, an \"identifier\" and a pair of \"void brackets [ ]\". For example, the following function: \n void procedure (int arg[] ) \n accepts a parameter of type \"array of int\" called \"arg\". In order to pass to this function an array declared as: \n int myArray [40]; \n it would be enough to write a call like this: \n procedure[myArray] \n " << endl;

  cout << "\n*********************\n" << endl;
  
  cout << "In a function declaration it is also possible to include multidimensional arrays. However, the declaration of a multidimensional array must have bounds for all dimensions except the first. For example, a fucntion with a 2d array as argument would be declared as: " << endl;

  cout << "void procecude(int myArray[ ][10])" << endl;

  cout << "\n And a fucntion with a tridimensional array as argument would be: " << endl;
  cout << "void procecude(int myArra[][10][12])" << endl;
  cout << "\n Notice that the first brackets [ ] are left blank while the following ones are not. This is so because the compiler must be able to determine within the function which is the depth of each additional dimension... " << endl;

  cout << "\n*********************\n" << endl;
} //end of: void instructions(void) {

void print1dArray(int myArray[], int length) {

  cout << "\n->Printing 1d Array...\n" << endl;

  for (int i = 0; i < length; i++){
    cout << myArray[i] << " " ;
  }
  
  cout << "\n" << endl;

} //end of: void printArray(int myArray[], int length) {

void print2dArray(int myArray[][10], int rows) {

  cout << "\n->Printing 2d Array...\n" << endl;

  for (int i = 0; i < rows; i++){
    for( int j=0; j < 10; j++){
       cout << " " << myArray[i][j] << " " ;
     }
    cout << "\n" << endl;
  }
  
} //end of: void print2dArray(int myArray[][10], int rows) {

