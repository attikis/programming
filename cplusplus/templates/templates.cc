// templates.cc
// see: http://www.cplusplus.com/doc/tutorial/templates/

// Tell the preprocessor to include the standard file iostream
#include <iostream>
#include <string>

// Load standard C++ libraries
using namespace std;

template < class myType>

// not that the function has to manipulate+return the same kind of variable/class.
myType GetMax(myType a, myType b) {
  return(a>b?a:b);
}

int main(){

  int myInteger;
  double myDouble;

  myInteger = GetMax(1, 2);
  myDouble = GetMax(1.24, 2.2001);
 
  cout << "myInteger = GetMax(1, 2) = " <<  GetMax(1, 2) << endl;
  cout << "myDouble = GetMax(1.24, 2.2001) = " <<  GetMax(1.24, 2.2001) << endl;

  // End of function
  return 0; 
}
