// overloading_operators.cc
#include <iostream>
using namespace std;

class CVector{
  
public:
  int x, y, z;
  CVector() {};
  CVector(int, int, int);
  CVector operator + (CVector);

};

// Define the constructor
CVector::CVector(int a, int b, int c){
  x = a;
  y = b;
  z = c;
}

// Overload the "+" operator to add two CVectors together and return another CVector object.
CVector CVector::operator+(CVector param){
  CVector tmp;
  tmp.x = x + param.x;
  tmp.y = y + param.y;
  tmp.z = z + param.z;
  
  return tmp;
}

int main(void){
  CVector a(3, -2, 0);
  CVector b(-3, 2, 1);
  CVector c = a + b;

  cout << "a.x = " << a.x << ", a.y = " << a.y << ", a.z = " << a.z << endl;
  cout << "b.x = " << b.x << ", b.y = " << b.y << ", b.z = " << b.z << endl;
  cout << "c.x = " << c.x << ", c.y = " << c.y << ", c.z = " << c.z << endl;
  
  return 0;

}
  
