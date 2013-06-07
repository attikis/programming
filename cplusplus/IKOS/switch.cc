#include <iostream>
#include <string>
using namespace std;

int main(){
  
  int i = 0;

  for(i=0; i < 20; i++){
    // std::cout << "0) i = " << i << std::endl;
    switch(i){
    case 0: 
      i+=5;
      // std::cout << "1) i = " << i << std::endl;
    case 1: 
      i+=2;
      // std::cout << "2) i = " << i << std::endl;
    case 5: 
      i+=5;
      // std::cout << "3) i = " << i << std::endl;
    default:
      i+=4;
      // std::cout << "4) i = " << i << std::endl;
      break;
    }
      printf("%d ,",i);
  }
  std::cout << "" << std::endl;
}


