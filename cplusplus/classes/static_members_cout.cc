// static_members_cout.cc
#include <iostream>

using namespace std;

class Verbose{

public:
  static int nObjects, nLines;
  Verbose(void);
  ~Verbose(void);
  void Cout(const string myMessage);
};

// Constructor
Verbose::Verbose(void){
  nObjects++;
}

// Destructor
Verbose::~Verbose(void){}

// This is needed!
int Verbose::nObjects=0;
int Verbose::nLines=0;
  
void Verbose::Cout(const string myMessage){
  cout << nObjects << "." << nLines << ") " << myMessage << endl;
  nLines++;
  return;
}

int main(void){
  
  Verbose v1;
  v1.Cout("test");
  v1.Cout("test");
  v1.Cout("test");
  v1.Cout("test");

  Verbose v2;
  v2.Cout("test");
  v2.Cout("test");
  v2.Cout("test");
  v2.Cout("test");

  
  return 0;
}
  
