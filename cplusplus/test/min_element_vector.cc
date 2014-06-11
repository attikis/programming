// min_element/max_element example
#include <iostream>     // std::cout
#include <algorithm>    // std::min_element, std::max_element
#include <vector>

bool myFn(int i, int j) { return i < j; }
struct myclass {
bool operator() (int i, int j) { return i < j; }
} myObj;


int main () {

std::vector<int> myInts;
myInts.push_back(3);
myInts.push_back(7);
myInts.push_back(2);
myInts.push_back(5);
myInts.push_back(6);
myInts.push_back(4);
myInts.push_back(9);

std::cout << "\n*** Using default comparison:" << std::endl; 
std::cout << "The smallest element is " << *std::min_element(myInts.begin(), myInts.end()) << '\n';
std::cout << "The largest element is "  << *std::max_element(myInts.begin(), myInts.end()) << '\n';

 
std::cout << "\n*** Using function myFn as comp:" << std::endl; 
std::cout << "The smallest element is " << *std::min_element(myInts.begin(), myInts.end(), myFn) << '\n';
std::cout << "The largest element is "  << *std::max_element(myInts.begin(), myInts.end(), myFn) << '\n';


std::cout << "\n*** Using object myObj as comp:" << std::endl; 
std::cout << "The smallest element is " << *std::min_element(myInts.begin(), myInts.end(), myObj) << '\n';
std::cout << "The largest element is "  << *std::max_element(myInts.begin(), myInts.end(), myObj) << '\n';
 
return 0;
}
