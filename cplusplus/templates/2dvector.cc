// 2dvector.cc

// Tell the preprocessor to include iostream
#include <iostream>
#include <vector>

using namespace std;

// main function declaration 
int main() {
  
  // declare vector
  vector< vector <int> > my2dvector;

  // fill vector with ints
  for (int i=0; i<=5; i++){
    my2dvector.push_back( vector<int>(i*i) );
  }
  
  // create vector iterator
  vector <int>::iterator it;
  vector <int>& innerList = my2dvector[0];
  
  it = innerList.begin(); // initialize iterator (column zero)

  cout << "my2dvector contains:" << endl;
  for ( it = innerList.end() ; it < innerList.end(); it++ ){
    // for ( it=my2dvector.begin() ; it < my2dvector.end(); it++ ){
    cout << " (*it) = " << (*it) << endl;
    cout << endl;
    }

  cout << "\nDone!" << endl;
  return 0;

} //end of: int main() {
