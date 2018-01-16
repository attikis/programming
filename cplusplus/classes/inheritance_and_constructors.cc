// inheritance_and_constructors.cc
#include <iostream>
using namespace std;

class mother {
public:
  mother (void){ cout << "mother: no parameters\n"; } // the default constructor
  mother (int a){ 
    a = 1;
    cout << "mother: int parameter a = " << a << "\n"; }
};


class daughter : public mother {
public:
  // daughter inherits from mother  using the default constructor
  daughter (int a){ a= -1; cout << "daughter: int parameter a = " << a << "\n\n"; } // nothing specified: calls default constructor of both "mother" and "daughter"
};


class son : public mother {
public:
  // son inherits from mother but using a user-defined constructor
  son (int a) : mother (a){ a=-5; cout << "son: int parameter a = " << a << "\n\n"; } // constructor specified: calls overloaded constructor of "mother" and that of "son"
};

int main () {
  
  daughter Maria(0);
  son Alexandros(0);
  
  return 0;
}
