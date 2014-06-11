// min_element/max_element example
#include <iostream>     // std::cout
#include <algorithm>    // std::min_element, std::max_element

bool myfn(int i, int j) { return i<j; }

struct myclass {
  bool operator() (int i,int j) { return i<j; }
} myobj;


int main () {

  double EtaRegionVals[]      = {-2.3, -2.1, -1.9, -1.7, -1.5, -1.3, -1.1, -0.9, -0.7, -0.5, -0.3, -0.1, +0.1, +0.3, +0.5, +0.7, +0.9, +1.1, +1.3, +1.5, +1.7, +1.9, +2.1, +2.3};
  const int EtaRegionValsSize = sizeof(EtaRegionVals)/sizeof(*EtaRegionVals);

  // using default comparison:
  std::cout << "The smallest element is " << std::min_element(EtaRegionVals, EtaRegionVals+EtaRegionValsSize ) << '\n';
  
  return 0;
}
