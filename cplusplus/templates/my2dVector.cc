// my2dVector.cc


#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;


// forward function declaration
void a2dVectorExample(void);
void my2dVector(void);
void test(void);

// main function declaration
int main(){
  
  cout << endl;
  a2dVectorExample();

  cout << endl;
  my2dVector();

  cout << endl;
  test();!

  cout << "\nProgram Termination!" << endl;
  return 0;
  
} //end of: int main(){

void a2dVectorExample(void){
  std::vector< std::vector<int> > v;
  
  for ( int i = 0; i < 10; i++ ) {
    v.push_back ( std::vector<int>() );
    
    for ( int j = 0; j < 10; j++ )
      v[i].push_back ( i + j );
  }
  std::vector< std::vector<int> >::iterator row_it = v.begin();
  std::vector< std::vector<int> >::iterator row_end = v.end();
  
  for ( ; row_it != row_end; ++row_it ) {
    std::vector<int>::iterator col_it = row_it->begin();
    std::vector<int>::iterator col_end = row_it->end();
    
    for ( ; col_it != col_end; ++col_it )
      std::cout<< std::setw ( 3 ) << *col_it;
      std::cout<<'\n';
  }

} //end of: void my2dVector(void){


void my2dVector(void){

  // create the rows of the 2d vector
  std::vector< std::vector<string> > v_myStrings;
  
  // rows
  for ( int i = 0; i < 2; i++ ) {
    v_myStrings.push_back ( std::vector<string>() ); // To access the row "i"
    
    // columns
    for ( int j = 0; j < 5; j++ )
      v_myStrings[i].push_back ( " test " ); // Fill the column "j" of row "i"
  }
  // initialize iterators for the row of the 2d Vector
  std::vector< std::vector<string> >::iterator row_it = v_myStrings.begin(); 
  std::vector< std::vector<string> >::iterator row_end = v_myStrings.end();
  
  for ( ; row_it != row_end; ++row_it ) {
    // initialize iterators for the columns of the 2d Vector
    std::vector<string>::iterator col_it = row_it->begin();
    std::vector<string>::iterator col_end = row_it->end();
    
    for ( ; col_it != col_end; ++col_it )
      std::cout<< std::setw ( 3 ) << *col_it;
      std::cout<<'\n';
  }

} //end of: void my2dVector(void){



void test(void){

  // create the rows of the 2d vector
  vector< vector<string> > v_myStrings;
  
  // rows
  for ( int i = 0; i < 2; i++ ) {
    v_myStrings.push_back ( vector<string>() ); // To access the row "i"
    
    // columns
    for ( int j = 0; j < 5; j++ )
      v_myStrings[i].push_back ( " test " ); // Fill the column "j" of row "i"
  }
  // initialize iterators for the row of the 2d Vector
  vector< vector<string> >::iterator row_it = v_myStrings.begin(); 
  vector< vector<string> >::iterator row_end = v_myStrings.end();
  
  for ( ; row_it != row_end; ++row_it ) {
    // initialize iterators for the columns of the 2d Vector
    vector<string>::iterator col_it = row_it->begin();
    vector<string>::iterator col_end = row_it->end();
    
    for ( ; col_it != col_end; ++col_it )
      cout<< setw ( 3 ) << *col_it;
      cout<<'\n';
  }

} //end of: void test(void){
