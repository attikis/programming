// dynamic_memory.cc
#include <iostream>
#include <new>
using namespace std;

int main(){

  // Variable Declaration
  int i, n; // declare int-type data
  int *p;   // declare a pointer that point to an int-type data
  
  // User input
  cout << "*** How many numbers would you like to type? ";
  cin >> i;
  
  // Dynamic Memory Allocation: C++ provides two standard methods to check if the allocation was successful
  // a) One is by handling exceptions (default) 
  // b) "nothrow" - when a memory allocation fails, instead of throwing a bad_alloc exception or terminating the program, 
  //                the pointer returned by new is a null pointer, and the program continues its execution.

  // Using this method an exception of type bad_alloc is thrown when the allocation fails. 
  p =  new (nothrow) int[i]; // if a non-positive integer is supplied program continues 
  // p =  new int[i]; // if a non-positive integer is supplied program crashes
  if (p==0)
    {
      cout << "*** Error: Memory could not be allocated." << endl;
    }
  else
    {
      for(n=0; n<i; n++){
	cout << "*** Enter number " << n+1 << ": ";
	cin >> p[n];
      }
      cout << "*** You have entered: ";
      for(n=0; n<i; n++){
	cout << p[n] << ", " ;
      }
      // Delete dynamic memory once it is no longer needed (to free alocated memory for other requests)
      delete[] p;
    }
  cout << "" << endl;
  return 0;
}



    
