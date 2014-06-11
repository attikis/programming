#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath> 


int FindNearestIndex(const unsigned int arraySize, double myArray[], double myEtaValue){
  
  // Variable declaration/initialisation
  int index   = -1;
  int counter = 0;
  std::vector<double> v_eta;
  std::vector<double> v_binWidth;
  v_eta.reserve(arraySize);
  v_binWidth.reserve(arraySize-1);

  // Convert array to vector to simplify things
  for(unsigned int i = 0; i< arraySize; i++){ v_eta.push_back( myArray[i]); }

  // Create a vector with the bin widths (difference between eta values used)
  for( std::vector<double>::iterator it = v_eta.begin(); it != v_eta.end()-1; it++){ v_binWidth.push_back( abs( *(it)-*(it+1) ) ); }
  
  // Loop over all eta values and find the array index with a value closest to a chosen Eta value
  std::vector<double>::iterator it_eta      = v_eta.begin();
  std::vector<double>::iterator it_binWidth = v_binWidth.begin();
  double best_diff = 9999.9;
  for( it_eta = v_eta.begin(); it_eta != v_eta.end(); it_eta++, it_binWidth++){

    double diff     = std::abs( *(it_eta) - myEtaValue );
    double binWidth = *(it_binWidth);

    if ( diff < best_diff ){ 
      std::cout << diff << std::endl;
      index     = counter;
      best_diff = diff;
    }
    counter++;
    
  }

  return index;
}


void forLoop(void){

  const unsigned int size = 200;
  std::vector< unsigned int > nTracks;
  nTracks.reserve(size);
  
  std::vector< double > cm;
  for(unsigned int f= 0; f <= size; f++){
    double value = f*0.02; // cm
    cm.push_back( value );
    std::cout << "value = " << value << std::endl;
  }
  
  return;
}


void count(void){

  int a = 0;
  
  std::cout << "a = " << a << std::endl;
  std::cout << "a++ = " << a++ << std::endl;
}


void divide(void){
  
  unsigned int i;

  std::vector<float> CaloEt;
  // for (int i = 0; i <= 20; i++){

  //   float et = i*10.0;
  //   CaloEt.push_back(et);
  // }

  // CaloEt.push_back(10.432);
  // CaloEt.push_back(20.122);
  // CaloEt.push_back(30.20);
  // CaloEt.push_back(44.01);
  CaloEt.push_back(0.0);
  CaloEt.push_back(1.0);
  // CaloEt.push_back(9.999);
  // CaloEt.push_back(10.00);
  // CaloEt.push_back(49.99);
  // CaloEt.push_back(50.00);
  // CaloEt.push_back(50.01);
  // CaloEt.push_back(100.01);
  // CaloEt.push_back(110.01);

  std::vector<float>::iterator et;
  for (et = CaloEt.begin(); et!= CaloEt.end(); et++){
    unsigned int index = (unsigned int) (*et/10.0);
    std::cout << "et = " << *et << ", index = " << index << std::endl;
  }
  
  return;
}


void booleanDeclarations(void){
  
  bool a = 3 > 2;
  bool b = 1 > 0.1;
  
  std::cout << "a = " << a << std::endl;
  std::cout << "b = " << b << std::endl;
  a = false;
  std::cout << "a = " << a << std::endl;
  std::cout << "b = " << b << std::endl;    

  return;
}

void eraseVectorElement(void){
  std::vector<int> myInts;
  myInts.push_back(1);
  myInts.push_back(2);
  myInts.push_back(3);
  myInts.push_back(4);
  
  std::vector<int> myIntsCopy = myInts;
  std::vector<int>::const_iterator it1;

  for (it1 = myInts.begin(); it1 != myInts.end(); it1++){
    
    std::cout << "*it1 = " << *it1 << std::endl;

    if (*it1 == 1){
    std::cout << "Before Erase) *it1 = " << *it1 << std::endl;
    it1 = myIntsCopy.erase(it1);
    std::cout << "After Erase) *it1 = " << *it1 << std::endl;
    it1--;
    std::cout << "After Decrement) *it1 = " << *it1 << std::endl;
    std::cout << "" << std::endl;
  }

  }


  return;
}


void eraseVectorElementAlt(void){
  std::vector<int> myInts;
  myInts.push_back(0);
  myInts.push_back(1);
  myInts.push_back(2);
  myInts.push_back(3);
  myInts.push_back(4);
  myInts.push_back(5);
  
  std::vector<int> myIntsCopy = myInts;
  std::vector<int>::const_iterator it1;

  for (it1 = myInts.begin(); it1 != myInts.end(); it1++){

    std::cout << "*it1 = " << *it1 << std::endl;

    if (*it1 == 1){
    std::cout << "Before: *it1 = " << *it1 << std::endl;
    myIntsCopy.erase(it1);
    std::cout << "After: *it1 = " << *it1 << std::endl;
    std::cout << "" << std::endl;
  }

  }


  return;
}


void compareVectorElements(void){
  
  std::vector<int> myInts;
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
  
  std::vector<int> myIntsCopy = myInts;
  std::vector<int>::const_iterator it1;
  std::vector<int>::const_iterator it2;
  
  for (it1 = myInts.begin(); it1 != myInts.end(); it1++){
    
    for (it2 = myIntsCopy.begin(); it2 != myIntsCopy.end(); it2++){

      if(*it1 == *it2){	std::cout << "HAIL MARY!" << std::endl;}

    }
  }

}




void vectorInLoop(void){
  


  for (int i=0; i < 3; i++){
    std::vector<int> myInts;
    for (int j=0; j < 10; j++){
      myInts.push_back(j);      
    }
    std::cout << "Vector.size() = " << myInts.size() << std::endl;
  }

  return;
}


int main(void){
  ////////////////////    0,    1,    2,    3,    4,    5,    6,    7,    8,    9,   10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20,   21,   22,   23
  double myEtaMap[] = {-2.3, -2.1, -1.9, -1.7, -1.5, -1.3, -1.1, -0.9, -0.7, -0.5, -0.3, -0.1, +0.1, +0.3, +0.5, +0.7, +0.9, +1.1, +1.3, +1.5, +1.7, +1.9, +2.1, +2.3};
  int arrayIndex    = -1;
  double myEtas[] = {-0.1, 0.0, 0.1};
 
  for( int i = 0; i < 3; i++){ 
    arrayIndex = FindNearestIndex(24, myEtaMap, myEtas[i] ); 
    std::cout << "---> arrayIndex = " << arrayIndex << std::endl;
  }
  
  // forLoop();
  // count();
  // divide();
  // booleanDeclarations();
  // eraseVectorElementAlt();
  // eraseVectorElement();
  // compareVectorElements();
  // vectorInLoop();

  return 0;
}
