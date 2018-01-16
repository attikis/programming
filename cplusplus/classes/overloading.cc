// overloading.cc
#include <iostream>
using namespace std;

class Rectangle{
private:
  int x, y;
public:
  Rectangle(int, int);
  Rectangle(int);
  Rectangle(void);
  int Area(void){return (x*y);}
};

// Default Constructor assumes pre-determined fixed values for the sides
Rectangle::Rectangle(void){
  x=5;
  y=5;
}

// Alternative constructor is a square of side a
Rectangle::Rectangle(int a){
  x=a;
  y=a;
}

// Another Alternative constructor requires the values of both sides to construct the rectangle
Rectangle::Rectangle(int a, int b){
  x = a;
  y = b;
}



int main(void){

  Rectangle recA(3,5);
  Rectangle recB(2);
  Rectangle recC; // no brackets required

  cout << "Rectangle Area = " << recA.Area() << endl;
  cout << "Rectangle Area = " << recB.Area() << endl;
  cout << "Rectangle Area = " << recC.Area() << endl;
  
  return 0;

}
