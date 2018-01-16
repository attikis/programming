// destructor.cc
#include <iostream>
using namespace std;

class Rectangle{

private:
  int *width, *height; // width and height are pointers to some data of type int
public:
  Rectangle(int, int);
  ~Rectangle();
  int area(void){return ( (*width)*(*height) );}
};

// Constructor
Rectangle::Rectangle(int x, int y){
  width   = new int;  // assign dynamic memory to width
  height  = new int;  // assign dynamic memory to width
  *width  = x; //dereference operator to get value of width (not memory address)
  *height = y; //dereference operator to get value of height (not memory address)
}

// Destructor
Rectangle::~Rectangle(){
  delete width;
  delete height;
}

int main(void){
  
  Rectangle recA(3,5);
  Rectangle recB(1,1);
  cout << "Area = " << recA.area() << endl;
  cout << "Area = " << recB.area() << endl;
  
  return 0;
}
