#include <iostream>
#include <sstream>
#include <string>
#include <typeinfo>

int main () {

  float b = 5.0;
  std::cout << "typeid(b).name() = " << typeid(b).name() << std::endl;

}
