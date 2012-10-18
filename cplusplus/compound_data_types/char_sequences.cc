// char_sequences.cc
// C++ Tutorials: http://cplusplus.com/doc/tutorial/ntcs/

// Tell the preprocessor to include iostream:
#include <iostream>

// Load standard C++ libraries:
using namespace std;

// definitions

// prototype function declaration
void instructions(void);

// main function declaration
int main() {

  instructions();

  char Greeting [ ] = { 'H', 'e', 'l', 'l', 'o', ',', ' ','\0'}; // null character indicates end of array
  char Question[ ] = "Please, enter your first name: ";
  char YourName[100]; // array is big but it can be terminated at any size smaller than 100 by using the null character '\0'

  cout << Question ;
  cin >> YourName;
  cout << Greeting << YourName << "!" << endl;

  cout << "\n\n\n-> Last Comment: Sequences of characters stored in \"char\" arrays can easily be converted into string objects just by using the assignment operator: \n string mystring; \n char myCharArray[ ] = \"Some Text ...blah ...\"; \n myString = myCharArray; " << endl;

  cout << "\nProgram Termination!" << endl;
  return 0;

} //end of: // main function declaration

void instructions(void) {

  cout << "\nInstructions" << endl;
  cout << "************\n" << endl;


  cout << "The C++ Standard Library implements a powerful string class, which is very useful to handle and manipulate strings of characters. However, because strings are in fact sequences of characters, we can represent them also as plain arrays of char elements. For example, the following array: \n char jenny[20]; \n s an array that can store up to 20 elements of type \"char\". Therefore, in this array, in theory, we can store sequences of characters up to 20 characters long. But we can also store shorter sequences. For example, jenny could store at some point in a program either the sequence \"Hello\" or the sequence \"Merry christmas\", since both are shorter than 20 characters. " << endl;

  cout << "\nTherefore, since the array of characters can store shorter sequences than its total length, a special character is used to signal the end of the valid sequence: the null character, whose literal constant can be written as \"\\0\" (backslash, zero). Our array of 20 elements of type \"char\", called \"jenny\", can be represented storing the characters sequences \"Hello\" and \"Merry Christmas\" as: \n Hello\\0 \n Merry Christmass\\0 \n After the valid content a null character ('\\0') has been included in order to indicate the end of the sequence." << endl; 

  cout << "\n-> N.B.: Double quoted strings (\") are literal constants whose type is in fact a null-terminated array of characters. So string literals enclosed between double quotes always have a null character (\"\\0\") automatically appended at the end. Therefore we can initialize the array of \"char\" elements called \"myword\" with a null-terminated sequence of characters by EITHER ONE of these two methods: \n char myword[ ] = { { 'H', 'e', 'l', 'l', 'o', '\\0' }; \n char myword [] = \"Hello\"; " << endl;

  cout << "\n In both cases the array of characters \"myword\" is declared with a size of 6 elements of type \"char\": the 5 characters that compose the word \"Hello\" plus a final null character ('\\0') which specifies the end of the sequence and that, in the second case, when using double quotes (\") it is appended automatically. " << endl;

  cout << "\n\n Assuming \"myChar\" is a \"char[ ]\" variable, expressions within a source code like: \n myChar = \"Hello\"; \n myChar[ ] = \"Hello\"; \n would not be valid, like neither would be: \n myChar = { 'H', 'e', 'l', 'l', 'o', '\\0' }; \n\n The reason for this may become more comprehensible once you know a bit more about pointers, since then it will be clarified that an array is in fact a constant pointer pointing to a block of memory. " << endl;

} //end of: void instructions(void) {
