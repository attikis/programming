// multiple_inheritance.cc
#include <iostream>
using namespace std;

class CPolygon {
protected:
  int width, height;
public:
  void set_values (int a, int b){ width=a; height=b;}
};

class COutput {
public:
  void output (int i);
};

void COutput::output (int i) {
  cout << i << endl;
}

// Create a class named CRectangle that inherits from classes CPolygon and COutput
class CRectangle: public CPolygon, public COutput {
public:
  int area (void){ return (width * height); }
};


// Create another class CTriangle that inherits from classes CPolygon and COutput
class CTriangle: public CPolygon, public COutput {
public:
  int area (){ return (width * height / 2); }
};


int main (void) {

  CRectangle rect;
  CTriangle trgl;

  rect.set_values (4,5);
  trgl.set_values (4,5);

  rect.output (rect.area());
  trgl.output (trgl.area());

  return 0;
}
