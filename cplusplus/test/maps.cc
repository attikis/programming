#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath> 
#include <map> 

void maps(void){

  typedef std::map<std::vector<std::string>, unsigned int> m_type;
  typedef std::map<std::vector<std::string>, unsigned int>::iterator it_type;

  m_type m_test;
  std::vector<std::string> v_strings_A;
  v_strings_A.push_back("test-1-A");
  v_strings_A.push_back("test-2-A");
  v_strings_A.push_back("test-3-A");

  std::vector<std::string> v_strings_B;
  v_strings_B.push_back("test-1-B");
  v_strings_B.push_back("test-2-B");
  v_strings_B.push_back("test-3-B");

  std::vector<std::string> v_strings_C;
  v_strings_C.push_back("test-1-C");
  v_strings_C.push_back("test-2-C");
  v_strings_C.push_back("test-3-C");

  m_test.insert( std::make_pair( v_strings_A, 1 ) );
  m_test[ v_strings_A ] = 1;
  m_test[ v_strings_B ] = 2;
  m_test[ v_strings_C ] = 3;

  for(it_type iterator = m_test.begin(); iterator != m_test.end(); iterator++) {
    // key
    std::cout << "iterator->first = " << iterator->first[0] << std::endl;
    std::cout << "iterator->first = " << iterator->first[1] << std::endl;
    std::cout << "iterator->first = " << iterator->first[2] << std::endl;

    // value
    std::cout << "\titerator->second = " << iterator->second << std::endl;
  }

  std::vector<std::string> v_strings_1;
  v_strings_1.push_back("test-1-A");
  v_strings_1.push_back("test-2-A");
  v_strings_1.push_back("test-3-A");

  std::vector<std::string> v_strings_2;
  v_strings_2.push_back("test-1-A");
  v_strings_2.push_back("test-2-A");
  v_strings_2.push_back("test-3-X");

  bool bFoundValue_1 = m_test.find( v_strings_1 ) != m_test.end(); 
  std::cout << "bFoundValue_1 = " << bFoundValue_1 << std::endl;

  bool bFoundValue_2 = m_test.find( v_strings_2 ) != m_test.end(); 
  std::cout << "bFoundValue_2 = " << bFoundValue_2 << std::endl;

  return;
}


int main(void){
  
  maps();

  return 0;
}
