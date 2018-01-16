// enumns.cc
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

// All months after january are assigned the value n+1
enum s_months {january=1, february, march, april, may, june, july, august, september, october, november, december};

int main(){
  s_months myMonths;
  
  myMonths = may;
  cout <<  "*** myMonths = " << myMonths << endl;

  return 0;
}
