// .cc
// link

// Tell the preprocessor to include iostream
#include <iostream>

using namespace std;

// main function declaration 
int main() {

  bool bCutOne = true;
  bool bCutTwo = true;
  bool bCutThree = true;
  bool bCutFour = false;
    
  bool bPassedCuts = bCutOne * bCutTwo * bCutThree * bCutFour;
  std::cout << "*** bPassedCuts = " << bPassedCuts << std::endl;


  return 0;

} //end of:
