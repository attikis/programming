// pointers.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/pointers/

// Tell the preprocessor to include iostream:
#include <iostream>

// Load Standard C++ libraries:
using namespace std;

// Definitions here:
#define PI 3.14159265

// prototype function declaration:
void instructions(void);
void myPointers(void);
void myPointers2(void);

// main function declaration: 
int main() { 
  
  instructions();
  myPointers();
  myPointers2();

  cout << "\nProgram Termination! " << endl;
  return 0;

}  // end of: int main() { 

// Auxiliary functions here: 
void instructions(void) {

  cout << "\nReference Operator(&)" << endl;
  cout << "*********************\n" << endl;

  cout << "As soon as we declare a variable, the amount of memory needed is assigned for it at a specific location in memory (its memory address). We generally do not actively decide the exact location of the variable within the panel of cells that we have imagined the memory to be - Fortunately, that is a task automatically performed by the operating system during runtime. However, in some cases we may be interested in knowing the address where our variable is being stored during runtime in order to operate with relative positions to it." << endl;
  cout << "\n The address that locates a variable within memory is what we call a reference to that variable. This reference to a variable can be obtained by preceding the identifier of a variable with an ampersand sign (&), known as \"reference operator\", and which can be literally translated as \"address of\". For example: \n ted = &andy; \n This would assign to ted the address of variable andy, since when preceding the name of the variable andy with the reference operator (&) we are no longer talking about the content of the variable itself, but about its reference (i.e., its address in memory). " << endl;

  cout << "\n Consider the following code fragment: \n andy = 25; \n fred = andy; \n ted = &andy; " << endl;

  cout << "First we have assigned the value 25 to \"andy\". We will ASSUME that this variable's address in memory is 1776. The second statement copies to \"fred\" the CONTENT of variable \"andy\". The third statement copies to \"ted\" NOT the value contained in \"andy\" but a REFERENCE to it (i.e. its memory address). The variable that stores the reference to another variable (like ted in this example) is what we call a \"pointer\". " << endl;

  cout << "\nDereference operator (*)" << endl;
  cout << "************************\n" << endl;

  cout << "A variable which stores a reference to another variable is called a \"pointer\". Pointers are said to \"point to\" the variable whose reference they store. Using a pointer we can directly access the value stored in the variable which it points to. To do this, we simply have to precede the pointer's identifier with an asterisk (*), which acts as \"de-reference\" operator and that can be literally translated to \"value pointed by\". \nTherefore, following with the values of the previous example, if we write: \n beth = *ted; \n (that we could read as: \"beth equal to value pointed by ted\") beth would take the value 25, since ted is 1776, and the value pointed by 1776 is 25. " << endl;


  cout << "\n->N.B.: You must differentiate that the expression \"ted\" refers to the memory address value 1776, while *ted (with an asterisk * preceding the identifier) refers to the VALUE stored at address 1776, which in this case is 25. Notice the difference of including or not including the \"dereference operator\". This can be read as:  \n " << endl;

  cout << "(remember: ted = &andy; So ted is a reference to andy ==> ted is a memory location and not a value) \n beth = ted;   // beth equal to ted ( 1776 ) \n beth = *ted;  // beth equal to value pointed by ted ( 25 ) " << endl;

  cout << "\n-->N.B.: Notice the difference between the reference and dereference operators: \n* & is the reference operator and can be read as \"address of\" \n * is the dereference operator and can be read as \"value pointed by\". Thus, they have complementary (or opposite) meanings. A variable referenced with & can be dereferenced with *." << endl;

  cout << "********************************************************************************\n" << endl;

} //end of: void instructions(void) {

void myPointers(void) {
  
  cout << "\nDeclaring variables of pointer types" << endl;
  cout << "************************************\n" << endl;
  
  int firstValue = 5;
  int secondValue = 15;
  int *v1, *v2;

  v1 = &firstValue; //read as: v1 is a reference to memory address variable "firstValue"
  v2 = &secondValue;
  
  *v1 = 10;          // value vointed by v1 = 10
  *v2 = *v1;         // value pointed by v2 = value pointed by p1
  v1 = v2;           // v1 = v2 (value of pointer is copied)
  *v1 = 20;          // value pointed by p1 = 20

  cout << "firstValue is = " << firstValue << endl;
  cout << "secondValue is = " << secondValue << endl;

  
  cout << "********************************************************************************\n" << endl;
  
}  //end of: void pointer() {

void myPointers2(void) {

  int firstValue = 5;
  int secondValue = 15;
  int *p1, *p2;

  cout << "firstValue is " << firstValue << endl;
  cout << "secondValue is " << secondValue << endl;
  cout << "\n" << endl;
  
  p1 = &firstValue;  // p1 = memory address of firstValue
  p2 = &secondValue; // p2 = memory address of secondValue

  cout << "firstValue is " << firstValue << endl;
  cout << "secondValue is " << secondValue << endl;
  cout << "p1 is " << p1 << " while *p1 is "<< *p1 << endl;
  cout << "p2 is " << p2 << " while *p2 is "<< *p2 << endl;
  cout << "\n" << endl;
  
  *p1 = 10;   // value pointed by p1 = 10 (=> value at memory location now changed)
  *p2 = *p1;  // value pointed by p2 = value pointed by p1 (but different memory location)

  cout << "firstValue is " << firstValue << endl;
  cout << "secondValue is " << secondValue << endl;
  cout << "p1 is " << p1 << " while *p1 is "<< *p1 << endl;
  cout << "p2 is " << p2 << " while *p2 is "<< *p2 << endl;
  cout << "\n" << endl;

  p1 = p2;           // p1 = p2 (value of pointer is copied => memory address now same)
  
  cout << "firstValue is " << firstValue << endl;
  cout << "secondValue is " << secondValue << endl;
  cout << "p1 is " << p1 << " while *p1 is "<< *p1 << endl;
  cout << "p2 is " << p2 << " while *p2 is "<< *p2 << endl;
  cout << "\n" << endl;

  *p1 = 20;  // value pointed by p1 = 20 (and hence by p2) 
  // note: p2 also notes at the same location but is assigned a different value.

  cout << "p1 is " << p1 << " while *p1 is "<< *p1 << endl;
  cout << "p2 is " << p2 << " while *p2 is "<< *p2 << endl;
  cout << "firstValue is " << firstValue  << endl;
  cout << "secondValue is " << secondValue << endl;
  cout << "\n" << endl;
  cout << "N.B. : p1 points to the memory location of the \"int\" firstValue, and hence when the value of the pointer to this memory address is changed by the command \"*p1=20;\" this in fact MODIFIES the value of firstValue ! " << endl;

    
  // First, we have assigned as value of p1 and p2 a reference to firstValue and 
  // secondValue respectively using the reference operator (&).
  // And then we have assigned the value 10 to the memory location pointed by p1, 
  // which because at this moment is pointing to the memory location of firstValue, 
  // this in fact MODIFIES the value of firstValue.
  // In order to demonstrate that a pointer may take several different values during the 
  // sample program I have repeated the process with secondValue and that same pointer, p1.

}  // end of: void myPointersExample(void) {
  
