// test_1.cc
#include <iostream>

class A
{
public:
    A(int n = 0) : m_n(n) {++m_ctor1_calls;}

    A(const A& a)
        : m_n(a.m_n)
    {
        ++m_copy_ctor_calls;
    }

public:
    static int m_ctor1_calls;
    static int m_copy_ctor_calls;

private:
    int m_n;
};

int A::m_ctor1_calls = 0;
int A::m_copy_ctor_calls = 0;

void f(const A &a1, const A &a2 = A())
{
}

int main()
{
  A a(2);
  A b = 5;
  //std::cout << "b = " << b << st::endl;
    const A c(a), &d = c, e = b;
    std::cout << A::m_ctor1_calls << A::m_copy_ctor_calls;
    b = d;
    A *p = new A(c), *q = &a;
    std::cout << A::m_copy_ctor_calls;
    delete p;
    f(3);
    std::cout << A::m_ctor1_calls << A::m_copy_ctor_calls << std::endl;

    return 0;
}
