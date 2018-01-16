// constructor.cc
#include <iostream>

using namespace std;

class Rectangle{
  
private:
  int width, height;
public:
  Rectangle(int, int);
  int Area(void ){return (width*height);}
};

// Declare the constructor. Must NOT have a return value (not even void). Called automatically as soon as a Class object is created
// Can use it to initialise any data type of the Class Rectangle. 
Rectangle::Rectangle(int a, int b){
  width = a;
  height = b;
}

int main(void){
  
  Rectangle rectA(3, 4);
  Rectangle rectB(9, 12);
  
  cout << "Rectangle area: " << rectA.Area() << endl;
  cout << "Rectangle area: " << rectB.Area() << endl;

  return 0;

}
