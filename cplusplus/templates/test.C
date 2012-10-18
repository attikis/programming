#include <iostream>

using namespace std;

void test();

int main(){

test();

 return 0;
}



void test(){


  for(int i=0; i<100; i++){
    std::cout << "Currently at i = " << i << std::endl;
    if(i ==50) return;
  }
}
