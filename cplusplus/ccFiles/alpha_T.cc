
// for_loop.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/control/

// Tell the preprocessor to load the iostream file
#include <iostream>
// Tell the preprocessor to load the stringstream file
#include <sstream>
// Tell the preprocessor to load the string file
#include <string>

// Load standard C++ libraries
using namespace std;

// main function declaration
int main () {


  
  for ( unsigned i=0; i < unsigned(1<<(5-1)); i++ ) { //@@ iterate through different combinations
    unsigned k = 1<<(5-1);
    std::cout << "i = " << i << "\t k = " << k << std::endl;
    //    double delta_sum_et = 0.;
    for ( unsigned j=0; j < 5; j++ ) { //@@ iterate through jets
      // delta_sum_et += et[j] * ( 1 - 2 * (int(i>>j)&1) ); 
	// if ( list ) { jet.push_back( (int(i>>j)&1) == 0 ); } 
      cout << "i = " << i << "\t j " << j << "\t(int(i>>j)&1) = " << (int(i>>j)&1) << std::endl;
    }
  }
  
  // program termination
  return 0;
  
} //end of: int main () {
