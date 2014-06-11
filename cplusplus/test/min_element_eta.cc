// min_element/max_element example
#include <iostream>     // std::cout
#include <algorithm>    // std::min_element, std::max_element
#include <vector>

int searchNearest(std::vector<double> myVector, double myEtaValue){
  
  int index = -1;
  for(int i = 0; i < myVector.size(); i++){

    if (myVector[i] >= myEtaValue){ 
      index = i;
      break; 
    }
    else{ continue; }
  }

  return index;

}


double GetWeights(double myEtValue, double myEtaValue){

  std::cout << "*** Et = " << myEtValue << ", Eta = " << myEtaValue << std::endl;

  /// Eta
  std::vector<double> EtaVals;
  EtaVals.push_back( -2.3 ); 
  EtaVals.push_back( -2.1 ); 
  EtaVals.push_back( -1.9 ); 
  EtaVals.push_back( -1.7 ); 
  EtaVals.push_back( -1.5 ); 
  EtaVals.push_back( -1.3 ); 
  EtaVals.push_back( -1.1 ); 
  EtaVals.push_back( -0.9 ); 
  EtaVals.push_back( -0.7 ); 
  EtaVals.push_back( -0.5 ); 
  EtaVals.push_back( -0.3 ); 
  EtaVals.push_back( -0.1 ); 
  EtaVals.push_back( +0.1 );
  EtaVals.push_back( +0.3 ); 
  EtaVals.push_back( +0.5 ); 
  EtaVals.push_back( +0.7 ); 
  EtaVals.push_back( +0.9 ); 
  EtaVals.push_back( +1.1 ); 
  EtaVals.push_back( +1.3 ); 
  EtaVals.push_back( +1.5 ); 
  EtaVals.push_back( +1.7 ); 
  EtaVals.push_back( +1.9 ); 
  EtaVals.push_back( +2.1 ); 
  EtaVals.push_back( +2.3 );
  int index = searchNearest( EtaVals, myEtaValue );
  std::cout << "index  = " << index << std::endl;

  /// Et
  double Et_LEQ20     [] = {1.71, 1.82, 1.64, 1.46, 1.07, 1.31, 1.37, 1.37, 1.31, 1.35, 1.54, 1.52, 1.42, 1.31, 1.26, 1.36, 1.51, 1.22, 1.15, 1.14, 1.39, 1.42, 1.34, 1.31};
  double Et_G20_LEQ40 [] = {1.10, 1.14, 1.19, 1.12, 0.89, 0.94, 1.07, 1.06, 0.99, 1.10, 1.08, 1.14, 1.16, 1.09, 1.09, 1.00, 1.02, 0.99, 0.92, 0.90, 1.15, 1.23, 1.11, 1.13};
  double Et_G40_LEQ60 [] = {1.01, 0.99, 1.05, 0.99, 0.84, 0.81, 0.87, 0.87, 0.93, 0.95, 0.98, 0.99, 0.96, 1.00, 0.96, 0.93, 0.89, 0.86, 0.86, 0.81, 1.00, 1.06, 1.01, 1.00};
  double Et_G60_LEQ80 [] = {0.98, 0.90, 0.96, 0.91, 0.75, 0.76, 0.77, 0.86, 0.84, 0.90, 0.87, 0.93, 0.94, 0.87, 0.88, 0.86, 0.78, 0.77, 0.76, 0.76, 0.88, 1.02, 0.89, 1.00};
  double Et_G80       [] = {0.91, 0.91, 0.66, 0.66, 0.65, 0.68, 0.71, 0.74, 0.75, 0.83, 0.77, 0.77, 0.77, 0.74, 0.72, 0.77, 0.76, 0.76, 0.71, 0.65, 0.71, 0.71, 0.75, 0.91};
  std::cout << "Et_LEQ20 [index] = "<<  Et_LEQ20 [index] << std::endl;

  if ( myEtValue <= 20.0){ return Et_LEQ20[index]; }
  else if ( 20.0 < myEtValue <= 40.0 ){ return Et_G20_LEQ40[index]; }
  else if ( 40.0 < myEtValue <= 60.0 ){ return Et_G40_LEQ60[index]; }
  else if ( 60.0 < myEtValue <= 80.0 ){ return Et_G60_LEQ80[index]; }
  else if ( 80.0 < myEtValue ){ return Et_G80[index]; } 
  else {
    std::cout << "Something went wrong! Exiting ..." << std::endl;
    exit(-1);
  }
  //else throw cms::Exception("LogicError") << "TauSelection: no or unknown operating mode! Options for 'operatingMode' are: 'standard', '


};


int main () {

  double EtWeight = GetWeights(10.8, -2.3);
  std::cout << "weight = " << EtWeight << std::endl;

  return 0;
}
