// operators.cc
// C++ Tutorial: http://cplusplus.com/doc/tutorial/operators/

// Tell the preprocessor to include the standard file iostream
#include <iostream>

// Load standard C++ libraries
using namespace std;

// main function declaration
int main() {

  // Arithmetic operators
  // ********************
  // The five Arithmetic operators ( +, -, *, /, % ) supported by C++ are:
  // +    addition
  // -    subtraction
  // *    multiplication
  // /    division
  // %    modulo

  // The "modulo" arithmeticoperator, given by the percentage sign (%) gives 
  // the remainder of a division of two values. For example, if we write:
  // a = 11 % 3;
  // the variable "a" will contain the value 2, since 2 is the remainder 
  // from dividing 11 between 3.

  cout << "\nArithmetic operators" << endl;
  cout << "********************\n" << endl;

  int a = 12;
  int b = 3;
  int c = 11;
  int d = 23;
  int e = 100;

  int result; 
  int remainder;

  result = a / b;
  remainder = a % b;
  
  cout << "Dividing " << a << " by " << b << " gives " << result << " and a remainder " << remainder << endl;

  result = e / d;
  remainder = e % d;

  cout << "\nDividing " << e << " by " << d << " gives " << result << " and a remainder " << remainder << endl;

  result = e / b;
  remainder = e % b;

  cout << "\nDividing " << e << " by " << b << " gives " << result << " and a remainder " << remainder << endl;

  // **********************************************************************
  
  cout << "\nCompound assignment" << endl;
  cout << "********************\n" << endl;
  
  // Compound assignment (+=, -=, *=, /=, %=, >>=, <<=, &=, ^=, |=)
  // When we want to modify the value of a variable by performing an 
  // operation on the value currently stored in that variable we can 
  // use compound assignment operators:
  // expression           |   is equivalent to
  // *****************************************************
  // value += increase;   |    value = value + increase;
  // a -= 5;              |    a = a - 5;
  // a /= b;              |    a = a / b;    
  // price *= units + 1;  |    price = price * (units + 1);

  a = 10;
  b = 20;
  
  cout << "If a = " << a << " and b = " << b << "\t ..." << endl;
  cout << "\n" << endl;
  
  // Examples of Compound operations
  a -= 5;
  b += 20;
  cout << "\"a -=5 ;\" gives " << a << "\n\"b += 20;\" gives " << b << endl;

  b /= a;

  cout << "\nA nd since the new values will remain in the memory replacing the old ones,\n \"b /= a; \" will now give " << b << endl;
  
  cout << "The values stored in the memory now for \"a\" and \"b\" are:\n a = "<< a << "\n b = "<< b << endl;
  
  // **********************************************************************
  
  cout << "\nRelation and Equality operators" << endl;
  cout << "********************************\n" << endl;
  
  // Relational and equality operators ( ==, !=, >, <, >=, <= ):
  // In order to evaluate a Comparison between two expressions we can use the 
  // relational and equality operators. The result of a relational operation 
  // is a Boolean value that can only be true or false.
  // We may want to compare two expressions, for example, to know if they are 
  // equal or if one is greater than the other is. Here is a list of the 
  // relational and equality operators that can be used in C++:  
  // ==  Equal to
  // !=  Not Equal to
  // >   Greater than
  // <   Less than
  // >=  Greater than OR Equal to
  // <=  Less than OR Equal to
  
  bool myStatus = 0;

  if ( 7 == 5 ) { myStatus = 1; }
    else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( 7 < 5 ) { myStatus = 1; }
    else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( 7 > 5 ) { myStatus = 1; }
  else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( 7 >= 5 ) { myStatus = 1; }
  else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( 7 <= 5 ) { myStatus = 1; }
  else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  // **********************************************************************
  
  cout << "\nLogical operators" << endl;
  cout << "*******************\n" << endl;

  // Logical operators ( !, &&, || )
  // The Operator "!" is the C++ operator to perform the Boolean operation 
  //NOT, it has only one operand, located at its right, and the only thing 
  // that it does is to inverse the value of it, producing false if its 
  // operand is "true" and "true" if its operand is "false". 
  // Basically, it returns the OPPOSITE boolean value of evaluating its 
  // operand. For example:
  // !(5 == 5)    // evaluates to false 
  // !(6 <= 4)    // evaluates to true because (6 <= 4) would be false. 
  // !true        // evaluates to false
  // !false       // evaluates to true.  

  if ( !(7 == 5 ) ) { myStatus = 1; }
    else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( !(7 < 5 ) ) { myStatus = 1; }
    else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( !(7 > 5 ) ){ myStatus = 1; }
  else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( !( 7 >= 5 ) ) { myStatus = 1; }
  else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;

  if ( !( 7 <= 5 ) ) { myStatus = 1; }
  else { myStatus = 0; }
  cout << "\n myStatus = " << myStatus << endl;
  
  // The logical operators "&&" and "||" are used when evaluating two 
  // expressions to obtain a single relational result. The operator "&&" 
  // corresponds with boolean logical operation "AND". This operation results 
  // true if BOTH its two operands are true, and false otherwise. 
  // The following panel shows the result of using "&&":
  bool trueBool  = 1;
  bool falseBool = 0;
  cout << "\n" << endl;
  cout << (trueBool && trueBool) << endl;
  cout << (trueBool && falseBool) << endl;
  cout << (falseBool && trueBool) << endl;
  cout << (falseBool && falseBool) << endl;
  
  // The following panel shows the result of using "||":
  cout << "\n" << endl;
  cout << (trueBool || trueBool) << endl;
  cout << (trueBool || falseBool) << endl;
  cout << (falseBool || trueBool) << endl;
  cout << (falseBool || falseBool) << endl;

  // The following panel shows the result of compining two expressions:
  
  cout << "\n" << endl;
  cout <<  ( (trueBool && trueBool) || (trueBool || trueBool) )      << endl;
  cout <<  ( (trueBool && falseBool) || (trueBool || falseBool) )    << endl;
  cout <<  ( (falseBool && trueBool) || (falseBool || trueBool) )    << endl;
  cout <<  ( (falseBool && falseBool) || (falseBool || falseBool) )  << endl;

  // **********************************************************************
  
  cout << "\nConditional operator" << endl;
  cout << "**********************\n" << endl;

  // The Conditional operator ( ? )
  // The conditional operator evaluates an expression returning a value if 
  // that expression is "true" and a different one if the expression is 
  // evaluated as "false". Its format is:
  //  condition ? result1 : result2
  // If condition is "true" the expression will return result1, 
  // if it is "false" it will return result2.

  cout << ( 7==5 ? 1 : 0 ) << endl;
  cout << ( 7>5  ? 1 : 0 ) << endl;
  cout << ( 7<5  ? 1 : 0 ) << endl;
  cout << ( 7>=5 ? 1 : 0 ) << endl;
  cout << ( 7<=5 ? 1 : 0 ) << endl;
  
  string yes = "yes";
  string no = "no";
  
  cout << "Is 12 gretarer than 5? " << ( ( 12 > 5) ? yes : no ) << endl;

  cout << "\n" << endl;
  // program termination 
  return 0;

} //end of: int main () { 
