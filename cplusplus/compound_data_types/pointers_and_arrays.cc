// pointers_and_arrays.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/pointers/

// Tell the preprocessor to include iostream:
#include <iostream>

// Load standard C++ libraries:
using namespace std;

// definitions here:
void instructions(void);
void demonstration(void);

// prototype function declaration here: 


// main function declaration here:
int main() {

  instructions();
  demonstration();

  cout << "\nProgram Termination!" << endl;
  return 0;

} // end of: int main() {

// auxiliary functions here: 
void instructions(void) {


  cout << "\nPointers and arrays" << endl;
  cout << "********************\n" << endl;

  cout << "The identifier of an array is equivalent to the address of its first element, as a pointer is equivalent to the address of the first element that it points to, so in fact they are the same concept. For example, supposing these two declarations: \n int numbers [20]; \n int *p; \n The following assignment operation would be valid: \n p = numbers; \n " << endl;

  cout << "After that, \"p\" and \"numbers\" would be equivalent and would have the same properties. The only difference is that we could change the value of pointer \"p\" by another one, whereas numbers will ALWAYS point to the first of the 20 elements of type \"int\" with which it was defined. Therefore, unlike \"p\", which is an ordinary pointer, \"numbers\" is an array, and an array can be considered a CONSTANT POINTER. Therefore, the following allocation would NOT be valid: \n numbers = p; \n " << endl;
  
  }  // end of: void instructions(void)

void demonstration(void) {

  int numbers[5]; // an array of 5 integers 
  int *p; // a pointer to an integer
  
  // fill the array with some random integers
  numbers[0] = 1988;
  numbers[1] = 14;
  numbers[2] = 21;
  numbers[3] = 50;
  numbers[4] = 90;

  cout << "->1<-" << endl;
  cout << " p is " << p << endl;
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  p = numbers;  // pointer p points to the same memory address as does the array 
                // of integers called "numbers" (which is a constant pointer)
  
  cout << "->2<-" << endl;
  cout << " p is " << p << endl;
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  *p = 10; // the pointer (i.e. the memory location) is assigned the value 10

  cout << "->3<-" << endl;
  cout << " p is " << p << " while (*p) is "<< (*p) << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  p++; // increment the value of the pointer => go one up on the memory array
       // p no longer point to the first array element. It points to the second element!

  cout << "->4<-" << endl;
  cout << " p is " << p << " while (*p) is "<< (*p) << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;

  *p = 20;

  cout << "->5<-" << endl;
  cout << " p is " << p << " while (*p) is "<< (*p) << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  p = &numbers[2];  // p is now assigned the 3rd element of the array
                    // equivalent to doing p++;
  
  cout << "->6<-" << endl;
  cout << " p is " << p << " while (*p) is "<< (*p) << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;

  *p = 30; // 3rd element of array now has the value 30

  cout << "->7<-" << endl;
  cout << " p is " << p << " while (*p) is "<< (*p) << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  p = numbers + 3; // point p now point to element 1+3 = 4
                   // remember, the "numbers" points to the beginnig of the memory block
  
  cout << "->8<-" << endl;
  cout << " p is " << p << " while (*p) is "<< (*p) << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  *p = 40;
  p = numbers; // pointer p agains points to the first element of array numbers.
  
  cout << "->9<-" << endl; 
cout << " p is " << p << " while *p is "<< *p << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  // currently p is pointing to the first element of numbers array
  *(p+4) = 50;  // p+4 pointer points to array elemet 1+4 = 5. i.e. the last one
                //  thus, last element of array is assigned the value 50.
  
  cout << "->10<-" << endl;
  cout << " p is " << p << " while (*p) is "<< (*p) << endl; 
  cout << " numbers[0] = " << numbers[0] <<  " numbers[1] = " <<  numbers[1] << " numbers[2] = " << numbers[2]  << " numbers[3] = " << numbers[3]  << " numbers[4] = " << numbers[4]  << endl;
  cout << "\n" << endl;
  
  for (int n=0; n < 5; n++){
      cout << "numbers["<< n <<"] = " << numbers[n] << endl;
    }

} // end of: void demonstration(void) {
