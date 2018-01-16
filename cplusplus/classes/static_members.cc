// static_members.cc
#include <iostream>

using namespace std;

class Whatever{

private:
  
public:
  static int n;
  Whatever(void){n++;};
  ~Whatever(void){n--;};
};

int Whatever::n=0;

int main(void){

  Whatever a;
  Whatever b[5]; //each initialisation (calls contructor) increments n by 1
  Whatever *c = new Whatever;

  cout << "a.n = " << a.n << endl;
  delete c; //each deletion (calls destructor) decreases n by 1

  cout << "Whatever::n = " << Whatever::n << endl;  
  
  return 0;
}
  
