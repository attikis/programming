// test_1.cc
#include <iostream>

class A{
public:
  A(int n = 0) : someInt(n) {++m_ctor1_calls;}
  A(const A& a) : someInt(a.someInt) {++m_copy_ctor_calls;}
  void Print(void){std::cout  << "someInt = " << someInt << std::endl;}
  // Nothing changes if i remove the term ": someInt(n)"
  // A(int n = 0){++m_ctor1_calls;} 
  // A(const A& a){++m_copy_ctor_calls;}

public:
  static int m_ctor1_calls;
  static int m_copy_ctor_calls;

private:
  int someInt;
};


int A::m_ctor1_calls = 0;
int A::m_copy_ctor_calls = 0;

void f(const A &a1, const A &a2 = A()){}


int main(){

  A testA;
  A a(testA);
  std::cout << "testA.m_ctor1_calls = " << testA.m_ctor1_calls << ", testA.m_copy_ctor_calls = " <<  testA.m_copy_ctor_calls << std::endl;
  std::cout << "a.m_ctor1_calls = " << a.m_ctor1_calls << ", testA.m_copy_ctor_calls = " <<  testA.m_copy_ctor_calls << std::endl;
  testA.Print();
  std::cout << "\n" << std::endl;

  A testB(10);
  A b(testB);
  std::cout << "testB.m_ctor1_calls = " << testB.m_ctor1_calls << ", testB.m_copy_ctor_calls = " <<  testB.m_copy_ctor_calls << std::endl;
  std::cout << "a.m_ctor1_calls = " << a.m_ctor1_calls << ", testB.m_copy_ctor_calls = " <<  testB.m_copy_ctor_calls << std::endl;
  testB.Print();
  std::cout << "\n" << std::endl;

  int blah;
  blah = int(10);
  std::cout << blah << std::endl;

  return 0;
}
