// friend_functions.cc
#include <iostream>

using namespace std;

class CRectangle{
private:
  int width, height;
public:
  void set_values(int, int);
  int area(void) {return (width*height);};
  friend CRectangle duplicate (CRectangle);
};

void CRectangle::set_values(int a, int b){
  
  width  = a;
  height = b;

  return;
}

CRectangle duplicate (CRectangle rectParam){
  
  CRectangle rectres;
  rectres.width = rectParam.width*2;
  rectres.height = rectParam.height*2;
  
  return rectres;
}

int main(void){
  CRectangle rect, rectb;
  rect.set_values(2,3);
  rectb = duplicate(rect);

  cout << "rect.area() = " << rect.area() << endl;
  cout << "rectb.area() = " << rectb.area() << endl;

  return 0;
}
  
