// remove_if example
#include <iostream>     // std::cout
#include <algorithm>    // std::remove_if
#include <vector>

int main () {

std::vector<int> myInts;
std::vector<int>::const_iterator it;
std::vector<int>::const_iterator it2;

myInts.push_back(1);
myInts.push_back(2);
myInts.push_back(3);
myInts.push_back(4);
myInts.push_back(5);
myInts.push_back(6);
myInts.push_back(7);
myInts.push_back(8);
myInts.push_back(9);
myInts.push_back(10);


for (it = myInts.begin(); it != myInts.end(); it++){
myInts.erase(it);
std::cout << "1) *it = " << *it << std::endl;
}

std::cout << "\n";
for (it2 = myInts.begin(); it2 != myInts.end(); it2++){
std::cout << "2) *it = " << *it2 << std::endl;
}

// myInts.erase(myInts.begin());
// for (it = myInts.begin(); it != myInts.end(); it++){
// std::cout << "*it = " << *it << std::endl;
// }

return 0;
}
