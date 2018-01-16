// inheritance.cc
#include <iostream>

using namespace std;

class Polygon{
private: //this cannot be accessed by friends
  
protected:
  int width, height;
public:
  void set_values(int a, int b){width =a; height=b;}
};

// Create the class Rectangle that inherits from polygon
class Rectangle: public Polygon{
public: //these are public variables of the class Rectange, in addition to those inherited from the class Polygon
  int area(void){return (width*height);}
};

class Triangle: public Polygon{
public:
  int area(void){return (width*height / 2);}
};

int main(void){
  
  Rectangle rectangle;
  Triangle triangle;

  rectangle.set_values(4,5);
  triangle.set_values(4,5);

  cout << "rectangle.area() = " << rectangle.area() << endl;
  cout << "triangle.area() = " << triangle.area() << endl;
  
  return 0;
}
  
