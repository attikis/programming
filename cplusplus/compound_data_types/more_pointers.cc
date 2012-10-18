// more_pointers.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/pointers/

// Tell the preprocessor to include iostream:
#include <iostream>

// Load standard C++ libraries:
using namespace std;

// Definitions here:

// prototype function declaration here:
void pointer_initialization (void);
void pointer_arithmetics (void);
void pointers_to_pointers (void);
void void_pointers (void);
void increase (void *data, int psize);
void pointers_to_functions( void );
int operation(int x, int y, int (*function_to_call)(int,int) );
int myAddition(int a, int b);
int subtraction(int a, int b);
int multiplication(int a, int b);

// main function declaration:
int main() {

  pointer_initialization();
  pointer_arithmetics();
  pointers_to_pointers();
  void_pointers();
  pointers_to_functions();

  // Program termination
  return 0;

} // end of: int main() {



void pointer_initialization(void){

  cout << "\nPointer Initialization" << endl;
  cout << "**********************\n" << endl;

  cout << " When declaring pointers we may want to explicitly specify which variable we want them to point to: " << endl;

  int number = 27;
  int *myAge = &number; // pass value by reference

  cout << " The declaration \n int number = 27; \n int *myAge = &number; \n is equivalent to: \n int number = 27; \n int *myAge; \n myAge = &number; " << endl;

  cout << " number = " << number << ", myAge = " << myAge << ", (*myAge) = " << (*myAge) << endl;
  myAge++; // i.e. myAge = myAge+1;
  cout << " myAge =  " << myAge << ", (*myAge) = " << (*myAge) << ", whereas number = " << number << endl;

  cout << "\n Since the value of \"number\" was passed by reference, the pointer cannot change the value of the variable \"number\". Incrementing the pointer changes the memory address of the pointer, which is un-assigned. \n" << endl;

  cout << "\n NOTE: When a pointer initialization takes place we are always assigning the reference value to where the pointer points (myAge), never the value being pointed to (*myAge). You must consider that at the moment of declaring a pointer, the asterisk (*) indicates only that it is a pointer, it is not the dereference operator (although both use the same sign: *). Remember, they are two different functions of one sign. So, writing: \n int number; \n int *myAge; \n *myAge  = &number \n is simply INCORRECT!" << endl; 

  cout << "\n\n As in the case of arrays, the compiler allows the special case that we want to initialize the content at which the pointer points with constants at the same moment the pointer is declared: \n char *myGreeting = \"hello \" ; " << endl;

  char *myGreeting = "hello";
  
  cout << "\n In this case, memory space is reserved to contain \"hello\" and then a pointer to the first character of this memory block is assigned to the pointer myGreeting. If we imagine that \"hello\" is stored at the memory locations that start at addresses 1702(for example), it is important to understand that the pointer \"myGreeting\" contains the value 1702, and NOT \"'h\" (memory address 1702) NOR \"e\" (memory address 1703) etc.. NOR \"hello\", although 1702 indeed is the address of both of \"h\" and \"hello\". "<< endl;

  cout << "\n The pointer myGreeting points to a sequence of characters and can be read as if it was an array (remember that an array is just like a constant pointer). For example: \n" << endl;

  cout << "(*myGreeting) = " << (*myGreeting) << endl;
  cout << "(*myGreeting+1) = " << (*(myGreeting+1)) << endl;
  cout << "(*myGreeting+2) = " << (*(myGreeting+2)) << endl;
  cout << "(*myGreeting+3) = " << (*(myGreeting+3)) << endl;
  cout << "(*myGreeting+4) = " << (*(myGreeting+4)) << endl;
  
  cout << "\n" ;
  
  for( int i = 0; i < 5; i++) {
    cout << *(myGreeting+i) ;
    if( i==4){ cout << "\n" << endl; }
  }

 cout << "\n ******************************************" << endl;
 
} //end of: void pointer_initialization() {


void pointer_arithmetics (void){

  cout << "\nPointer Arithmetics" << endl;
  cout << "*******************\n" << endl;

  cout << " The only arithmetical operations allowed to be performed on pointers are addition and subtraction, the others make no sense in the world of pointers. But both addition and subtraction have a different behavior with pointers ACCORDING TO THE SIZE of the data type to which they point. When we saw the different fundamental data types, we saw that some occupy more space than others in the memory. \n For example, let's assume that in a given compiler for a specific machine, \"char\" takes 1 byte, \"short\" takes 2 bytes and \"long\" takes 4. Suppose that we define three pointers in this compiler: \n char *mychar; \n short *myshort; \n long *mylong; " << endl;
char *myChar;
short *myShort;
long *myLong;
 
 cout << "And that we know that they point to memory locations 1000, 2000 and 3000 respectively. " << endl;
 
 myChar++;   //same as: myChar = myChar + 1;
 myShort++;  //same as: myShort = myShort + 1;
 myLong++;   //same as: myLong = myLong + 1;

 cout << "\n So, if we write: \n myChar++; \n myShort++; \n myLong++; \n \n \"myChar\", as you may expect, would contain the value 1001. But not so obviously, \"myShort\" would contain the value 2002, and \"myLong\" would contain 3004, even though they have each been increased only once. The reason is that when adding one to a pointer we are making it to point to the following element of the same type with which it has been defined, and therefore the size in bytes of the type pointed is added to the pointer. This is applicable both when adding and subtracting any number to a pointer. It would happen exactly the same if we write: \n" << endl;
 
 int random = 9;
 int *p = &random;

 cout << " NOTE: Both the increase (++) and decrease (--) operators have greater operator precedence (i.e. are executing FIRST)  than the dereference operator (*), but both have a special behavior when used as suffix (the expression is evaluated with the value it had before being increased). Therefore, the following expression may lead to confusion: \n *p++; \n (*p)++; \n " << endl;

 cout << "p = " << p << ", (*p) = " << (*p) << endl;
 cout << "*p++ = " << *p++ << ", (*p)++ = " << (*p)++ << ", but \n p = " << p << endl;

 cout << "\n Because ++ has greater precedence than *, the \n expression *p++ \n is equivalent to *(p++). Therefore, what it does is to increase the value of p (so it now points to the next element), but because ++ is used as postfix the whole expression is evaluated as the value pointed by the original reference (the address the pointer pointed to before being increased). Therefore: \n" << endl;

 cout << "*p++ = " << *p++ << " is equivalent to:  *(p++) = " << *(p++) << endl;

 cout << "\n Notice the difference with  (*p)++.  Here, the expression would have been evaluated as the value pointed by p increased by one. The value of p (the pointer itself) would not be modified (what is being modified is what it is being pointed to by this pointer). " << endl;

 cout << "(*p)++ = " << (*p)++ << " , whereas p = " << p << endl;
 
 cout << "\n To clarify things even more here is another example: \n If we write: \n *p++ = *q++; \n Because ++ has a higher precedence than *, both p and q are increased, but because both increase operators (++) are used as postfix and not prefix, the value assigned to *p is *q BEFORE both p and q are increased. And THEN both are increased. It would be roughly equivalent to: \n *p = *q; \n ++p; \n ++q; " << endl;

 cout << "\n -->Example: \n int value1 = 5; \n int value2 = 10; \n int *a = &value1; \n int *b = &value2; "<< endl;
 
 int value1 = 5;
 int value2 = 10;
 int *a = &value1;
 int *b = &value2;

 cout  << "a = " << a << " , (*a) = " << (*a) << endl;
 cout  << "b = " << b << " , (*b) = " << (*b) << endl;

 *a++ = *b++;
 cout << "\n *a++ = *b++;" << endl;

 cout  << "a = " << a << " , (*a) = " << (*a) << endl;
 cout  << "b = " << b << " , (*b) = " << (*b) << endl;

 cout << "\n ******************************************" << endl;

} //end of: void pointer_arithmetics (void){


void pointers_to_pointers(void) {

  cout << "\nPointers to pointers" << endl;
  cout << "********************\n" << endl;

  cout << " C++ allows the use of a pointer that points to another pointer, which in its turn points to data (or even to another pointer). In order to do that, we only need to add an asterisk (*) for each level of reference in their declarations: \n char a; \n char *b; \n char **c; \n a = 'z'; \n b = &a; \n c = &b; \n " << endl;

  char a = 'a';
  char anotherChar = 'B';  
  char *b;
  char **c;

  b = &anotherChar;
  c = &b;

  cout << " a = " << a << ", b = " << b << ", c = " << c << endl;
  cout << " (*b) = " << (*b) << ", (*c) = " << (*c) << endl;

  cout << "\n The new thing in this example is variable c, which can be used in THREE different levels of indirection, each one of them would correspond to a different value: (Assume memory locations for a 7230, for b 8092 and for c 10502. \n   c has type char** and a memory value of 8092. \n  *c has type char* and a memory location of 7230 \n **c has type char and a value of 'B' " << endl;
  
  cout << "\n c = " << c << endl;
  cout << "\n *c = " << (*c) << endl;
  cout << "\n **c = " << *(*c) << endl;

 cout << "\n ******************************************" << endl;

} //end of: void pointers_to_pointers(void) {


void void_pointers (void){

  cout << "\nVoid Pointers" << endl;
  cout << "**************\n" << endl;

  cout << " The void type of pointer is a special type of pointer. In C++, void represents the absence of type, so void pointers are pointers that point to a value that has no type (and thus also an undetermined length and undetermined dereference properties). \n This allows void pointers to point to ANY data type, from an integer value or a float to a string of characters. BUT in exchange they have a great limitation: the data pointed by them CANNOT be directly dereferenced (which is logical, since we have no type to dereference to), and for that reason we will always have to \"cast the address in the void pointer to some other pointer type that points to a concrete data type\" before dereferencing it." << endl;

  cout << " One of its uses may be to pass generic parameters to a function. " << endl;
  char aChar = 'x';
  int anInt = 1602;
  double aDouble = 10.0;
  short aShort = 50;
  long aLong = 100000000;

  cout << "\n aChar = " << aChar << " , anInt = " << anInt << endl;
  
  // call the 'increase' function
  increase( &aChar , sizeof(aChar) );
  increase( &anInt , sizeof(anInt) );
  increase( &aDouble , sizeof(aDouble) );
  increase( &aShort , sizeof(aShort) );
  increase( &aLong , sizeof(aLong) );
  
  cout << "\n aChar = " << aChar << " , anInt = " << anInt << endl;
  cout << " aLong = " << aLong << " , aShort = " << aShort << endl;
  cout << " aDouble = " << aDouble << endl;
  
  cout << "\n ******************************************" << endl;

} //end of: void void_pointers (void){


void increase (void *data, int psize) {
  
  cout << "\n MESSAGE from: void increase( void *data, int psize) \n sizeof is an operator integrated in the C++ language that returns the size in bytes of its parameter. For non-dynamic data types this value is a constant. Therefore, for example, sizeof(char) is 1, because char type is one byte long." << endl;
  
  if ( psize == sizeof(char) ){
    cout << " The variable inputted to this function is of type \"character\" " << endl;
    char *pchar;
    pchar = (char*)data; //cast the address in the void pointer to a pointer of type char  
    ++(*pchar); //increment the value of the variable by 1
  } //end of:     if ( psize == sizeof(char) ){
  
  else if ( psize = sizeof(int) ) {
    cout << " The variable inputted to this function is of type \"int\" " << endl;
    int *pint;
    pint = (int*)data; // cast the address in the void pointer to a pointer of type int
    ++(*pint);  //increment the value of the variable by 1
  } //end of:     else if ( psize = sizeof(int) ) {
  
  else if ( psize = sizeof(short) ) {
    cout << " The variable inputted to this function is of type \"short\" " << endl;
    short *pshort;
    pshort = (short*)data; // cast the address in the void pointer to a pointer of type short
    ++(*pshort);  //increment the value of the variable by 1
  } //end of:     else if ( psize = sizeof(short) ) {
  
  else if ( psize = sizeof(long) ) {
    cout << " The variable inputted to this function is of type \"long\" " << endl;
    long *plong;
    plong = (long*)data; // cast the address in the void pointer to a pointer of type long
      ++(*plong);  //increment the value of the variable by 1
  } //end of:     else if ( psize = sizeof(long) ) {
  
  else if ( psize = sizeof(double) ) {
    cout << " The variable inputted to this function is of type \"double\" " << endl;
    double *pdouble;
    pdouble = (double*)data; // cast the address in the void pointer to a pointer of type double
    ++(*pdouble);  //increment the value of the variable by 1
  } //end of:     else if ( psize = sizeof(double) ) {
    
  cout << " Exiting function \"increase\" ... " << endl;

} //end of: void increase (void *data, int psize){

void pointers_to_functions( void ) {

  cout << "\nPointers to functions" << endl;
  cout << "*********************\n" << endl;
  
  cout << " C++ allows operations with pointers to functions. The typical use of this is for \" passing a function as an argument to another function\", since these cannot be passed dereferenced. In order to declare a pointer to a function we have to declare it like the prototype of the function except that the name of the function is enclosed between parentheses () and an asterisk (*) is inserted before the name. For example: \n " << endl;

  int m, n;
  int (*minus)(int,int) = subtraction; //create a pointer to the function subtraction with the name 'minus'
  m = operation (5, 2, subtraction);
  m = operation (5, 2, minus);
  m = operation (5, 2, myAddition);
  m = operation (5, 2, multiplication);

  cout << "\n ******************************************" << endl;

}  //end of: void pointers_to_functions( void ) {


int myAddition(int a, int b) { return (a+b);}
int subtraction(int a, int b) { return (a-b);}
int multiplication(int a, int b) { return (a*b);}
int operation(int x, int y, int (*function_to_call)(int,int) ){
  int z ;
  z = (*function_to_call)(x,y);
  cout << "\n MESSAGE from: int operation() \n z = " << z << endl;
  return (z);
}
