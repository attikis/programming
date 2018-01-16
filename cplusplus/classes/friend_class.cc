// friends_classes.cc
#include <iostream>

using namespace std;

class CSquare;

class CRectangle {
private:
  int width, height;
public:
  int area(void){return (width * height);}
  void convert (CSquare a);
};

class CSquare {
private:
  int side;
public:
  void set_side (int a){side=a;}
  friend class CRectangle;
};

void CRectangle::convert (CSquare a) {
  width  = a.side;
  height = a.side;
}
  
int main () {

  CSquare sqr;
  CRectangle rect;

  // class "CSquare" does not have an "area" function. class "CRectangle" does have an "area" function
  sqr.set_side(4);

  // Use the fact that CSquare is "friends" with CRectangle, and use the latter's "convert" and "area" method
  rect.convert(sqr); 
  cout << rect.area() << endl;

  return 0;
}
