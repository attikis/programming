// classI.cc

#include <iostream>
#include <sstream>

using namespace std;

class Rectangle{
private:
  int x, y;
public:
  void set_values(int, int);
  int area(void){return (x*y);}
};

void Rectangle::set_values(int a, int b){
  x = a;
  y = b;
}

int main(void){

  int myX, myY;
  Rectangle myR;
  cout << "*** Enter x-value for rectangle: ";
  cin >> myX;

  cout << "*** Enter y-value for rectangle: ";
  cin >> myY;
  
  myR.set_values(myX, myY);
  cout << "*** Rectangle Area is " << myR.area() << endl;

  return 0;
}
