// arrays.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/arrays/

// Tell the preprocessor to include the file iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;

// forward prototype function declaration
void instructions(void);
void arrayExample(void);

// main fucntion declaration
int main() {

  instructions();
  
  arrayExample();

  cout << "\n Program Termination!" << endl;
  return 0;

}  // end of: int main () {

void instructions(void) {

  cout << "\nArrays" << endl;
  cout << "******\n" << endl;
  
  cout << "\nAn array is a series of elements of the SAME type placed in contiguous memory locations that can be individually referenced by adding an index to a unique identifier. That means that, for example, we can store 5 values of type \"int\" in an array without having to declare 5 different variables, each one with a different identifier. Instead of that, using an array we can store 5 different values of the same type, \"int\" for example, with a unique identifier. The elements of an array which contains N elements in total are numbered from 0 to N-1, since in arrays the first index is always 0, independently of its length. " << endl;

  cout << "\nLike a regular variable, an array must be declared before it is used. A typical declaration for an array in C++ is:" << endl;
  cout << "type name [Number of elements];" << endl;
  cout << "where \"type\" is a valid variable type (int, double float, char etc..) and the \"elements\" field  specifies how MANY of these elements the array has to contain ;" << endl;
  cout << "\nTherefore, in order to declare an array called \"myArray\" it is as simple as: " << endl;

  cout << " int myArray[5]; " << endl; 

  cout << "\nInitializing arrays" << endl;
  cout << "*******************" << endl;
  
  cout << "When declaring a regular array of local scope (within a function, for example), if we do not specify otherwise, its elements will not be initialized to any value by default, so their content will be undetermined until we store some value in them. The elements of \"global\" and \"static\" arrays, on the other hand, are automatically initialized with their default values, which for all fundamental types this means they are filled with zeros. " << endl;

  cout << "In both cases, \"local\" and \"global\", when we declare an array, we have the possibility to assign initial values to each one of its elements by enclosing the values in braces { }. For example: " << endl;

  cout << "int myArray [5] = { 16, 2, 77, 40, 12071 };" << endl;

  cout << "When an initialization of values is provided for an array, C++ allows the possibility of leaving the square brackets empty [ ]. In this case, the compiler will assume a size for the array that matches the number of values included between braces { }:" << endl;

  cout << "int myArray [ ] = { 16, 2, 77, 40, 12071 };" << endl;
  
  cout << "\nAccessing the values of an array." << endl;
  cout << "***********************************" << endl;
  cout << " In any point of a program in which an array is visible, we can access the value of any of its elements individually as if it was a normal variable, thus being able to both read and modify its value. To access the first element of the array you write: " << endl;
  cout << " myArray[0] " << endl;
  cout << "More generically, to access the \"nth\" element of an array carrying \"n\" elements you write: " << endl;
  cout << " myArray[n-1] " << endl;

  cout << "\n Therefore, if you want to assing a specific value to an array element you write: " << endl;
  cout << " myArray[2] = 75; " << endl;
  cout << "and, for example, to pass the value of the third element of myArray to a variable called \"a\", we could write: " << endl;
  cout << " a = myArray[2] ; " << endl;
    
  cout << "\n At this point it is important to be able to clearly distinguish between the two uses that brackets [ ] have related to arrays. They perform two different tasks: one is to specify the size of arrays when they are declared; and the second one is to specify indices for concrete array elements. Some other valid operations with arrays:" << endl;

  cout << " myArray[0] = a; \n myArray[a] = 75; \n b = myArray[a+2]; \n myArray[myArray[a]] = myArray[2] + 5; "<< endl;


  cout << "\n*******************************************************************************\n" << endl;
  
} //end of: void instructions(void) {

void arrayExample(void) {
  
  cout << "Executing an array example:" << endl;

  // array declaration 
  int myArray [ ] = { 2, 4, 6, 8, 10};
  int Sum = 0;
  
  for( int i = 0; i<5; i++) {
    
    Sum += myArray[i];   // add up all the elements in the array
    
  } //end of:   for( int i = 0; i<10; i++) {
  cout << "\n The Sum of all the elements in the array is: " << Sum << endl; 

} //end of: void arrayExample(void) {

