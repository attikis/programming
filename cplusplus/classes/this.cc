// this.cc
#include <iostream>

using namespace std;

class CDummy{

private:
  int x, y;
public:
  int IsItMe (CDummy &param);
};

int CDummy::IsItMe(CDummy &param){
  if (&param == this){
    cout << "Yes, it is me" << endl;   
    return true;
  }
  else{
    cout << "No, it's not me" << endl;  
    return false;
  }
}

int main(void){

  CDummy a;
  CDummy *b = &a;
  CDummy *c;

  b->IsItMe(a);
  c->IsItMe(a);

  return 0;
}
