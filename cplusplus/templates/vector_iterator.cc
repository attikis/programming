// vector_iterator.cc
// link

// Tell the preprocessor to include iostream
#include <iostream>

#include <vector>

using namespace std;

// main function declaration 
int main() {
  
  // declare vector
  vector<int> myvector;

  // fill vector with ints
  for (int i=1; i<=5; i++){
   myvector.push_back(i*i);
  }
  
  // create vector iterator
  vector<int>::iterator it;
  
  cout << "myvector contains:" << endl;
  
  for ( it=myvector.begin() ; it < myvector.end(); it++ )
    cout << " " << (*it) << endl;

  cout << endl;


  cout << "\n Program Termination! " << endl;
  return 0;

} //end of: int main() {
