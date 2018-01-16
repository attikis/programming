// compile    : [attikis]> g++ test.cc -o test
// permissions: [attikis]> chmod +x test
// execute    : [attikis]> ./test
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath> 
#include <math.h> // for fabs
#include <iomanip>

using namespace std;


void findTrigger(void){
  
  std::string matchTrg   = "HLT_PFHT450_SixJet40_BTagCSV_p056_v";
  std::vector<std::string> myTriggers;
  
  myTriggers.push_back("HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v3");
  myTriggers.push_back("HLT_PFHT450_SixJet40_BTagCSV_p056_v2");
  myTriggers.push_back("HLT_PFHT400_SixJet30_v2");
  myTriggers.push_back("HLT_PFHT450_SixJet40_v1");
  

  for (std::vector<string>::iterator t=myTriggers.begin(); t!=myTriggers.end(); t++)
    {
      size_t pos = (*t).find(matchTrg);
      cout << "trigger = " << *t << ", pos = " << pos << endl;
    }
  
  return;
  
}


template<typename T> void print(T t, const int& width=10)
{
  const char separator = ' ';
  // cout << left << setw(width) << setfill(separator) << t;
  cout << setprecision(3) << left << setw(width) << setfill(separator) << t;
}


void AlignText(void)
{

  const char separator    = ' ';
  const int nameWidth     = 6;
  const int numWidth      = 8;
  
  // cout << left << setw(nameWidth) << setfill(separator) << "Bob";
  // cout << left << setw(nameWidth) << setfill(separator) << "Doe";
  // cout << left << setw(numWidth) << setfill(separator) << 10.96;
  // cout << left << setw(numWidth) << setfill(separator) << 7.61;
  // cout << left << setw(numWidth) << setfill(separator) << 14.39;
  // cout << left << setw(numWidth) << setfill(separator) << 2.11;
  // cout << left << setw(numWidth) << setfill(separator) << 47.30;
  // cout << left << setw(numWidth) << setfill(separator) << 14.21;
  // cout << left << setw(numWidth) << setfill(separator) << 44.58;
  // cout << left << setw(numWidth) << setfill(separator) << 5.00;
  // cout << left << setw(numWidth) << setfill(separator) << 60.23;
  // cout << endl;
  std::cout << std::string(10*11, '=') << std::endl; 
  print("Pt");
  print("Eta");
  print("Phi");
  print("PdgId");
  print("Charge");
  print("z0");
  print("z0-prod");
  print("d0");
  print("d0-prod");
  print("dxy");
  cout << endl;  
  std::cout << std::string(10*11, '=') << std::endl;
  
  print(58.6771);
  print(2.71843);
  print(0.594244);
  print(-15);
  print(1);
  print(-0.822644);
  print(-0.820328);
  print(-0.000228737);
  print(0.065870);
  print(0.000483479);
  cout << endl;  


  // print("Bob", nameWidth);
  // print("Doe", nameWidth);
  // print(10.96, numWidth);
  // print(17.61, numWidth);
  // print(14.39, numWidth);
  // print(2.11, numWidth);
  // print(47.30, numWidth);
  // print(14.21, numWidth);
  // print(44.58, numWidth);
  // print(5.00, numWidth);
  // print(60.23, numWidth);
  // cout << endl;  
  // // cin.get();
  
  return;
}


void MinMax(void)
{
  double value1 = 5.0;
  double value2 = 15.0;
  
  std::cout << "Min = " << std::min(value1, value2) <<std::endl;
  std::cout << "Max = " << std::max(value1, value2)<< std::endl;
  
  return;
}

void Pow(void){

  int Z       = pow(2, 0);
  int W       = pow(2, 1);
  int top     = pow(2, 2);
  int HPlus   = pow(2, 3);
  int Unknown = pow(2, 4);

  std::cout << "\tZ = " << Z << std::endl;
  std::cout << "\tW = " << W << std::endl;
  std::cout << "\ttop = " << top << std::endl;
  std::cout << "\tHPlus = " << HPlus << std::endl;
  std::cout << "\tUnknown = " << Unknown << std::endl;
  return;
}

  
void MaxElement(void){

  double nums[] = {10.0, 20.0, 50.0, 1.0, 2.0, 0.0, -1.0};
  std::vector<double> v (nums, nums+6);
  
  
  for (int i=0; i < v.size(); i++){
    std::cout << "v.at(" << i << ") = " << v.at(i) << std::endl;
  }

  std::vector<double>::iterator v_it = std::max_element(v.begin(), v.end());

  
  std::cout << "max element =  " << *v_it << std::endl;
  std::cout << "max element position =  " << v_it - v.begin()  << std::endl;

  return;  
}



void Reference(double &b){

  double *a;
  a = &b;

  std::cout << "a = " << *a << std::endl;
  return;  
}

  void PixelAlgorithm(void){

  double myHitPos[] = {10.1, -2.2, 1.3, -0.3, 0.2, 1.8, 2.1, 13.3, 3.4, 8.2, 2.0, 2.1, 2.9, 1.0, 2.0};
  // std::vector<double> OAhits;
  std::vector<double> hitL1 (myHitPos, myHitPos+14);
  std::vector<double> hitL2 (myHitPos, myHitPos+10);
  std::vector<double> hitL3 (myHitPos, myHitPos+ 9);
  std::vector<double> hitL4 (myHitPos, myHitPos+ 4);
  std::vector<double> hitD1 (myHitPos, myHitPos+10);
  std::vector<double> hitD2 (myHitPos, myHitPos+ 8);
  std::vector<double> hitD3 (myHitPos, myHitPos+ 6);
  
  // Create an array of vectors to hold the pixel hits (descending order wrt occupancy)
  std::vector<double> hits[7];
  bool barrel[7];

  barrel[0]=true;
  barrel[1]=true;
  barrel[2]=true;
  barrel[3]=true;
  barrel[4]=false;
  barrel[5]=false;
  barrel[6]=false;

  hits[0]=hitL1;
  hits[1]=hitL2;
  hits[2]=hitL3;
  hits[3]=hitL4;
  hits[4]=hitD1;
  hits[5]=hitD2;
  hits[6]=hitD3;

  std::cout  << "*** Before bubble sort:" << std::endl;
  for (int i=0; i<7; i++) {
    std::cout  << "\thits[" << i << "].size() = " << hits[i].size() << " (barrel = " << barrel[i] << ")" << std::endl;
  }

  //sort on number of hits per layer
  bool more=false;
  do {
    more=false;
    for(int i=0;i<6;i++) {
      if (hits[i].size()<hits[i+1].size()) {
        more=true;
        std::vector<double> tmp=hits[i];
        hits[i]=hits[i+1];
        hits[i+1]=tmp;
        bool tmpb=barrel[i];
        barrel[i]=barrel[i+1];
        barrel[i+1]=tmpb;
      }
    }
  } while(more);
  

  std::cout  << "*** After bubble sort:" << std::endl;
  for (int i=0; i<7; i++) {
    std::cout  << "\thits[" << i << "].size() = " << hits[i].size() << " (barrel = " << barrel[i] << ")" << std::endl;
  }

  // Test for Anders's bug!
  for (int i=0; i<7; i++) {
    std::cout  << "\thits[" << i << "].size() = " << hits[i].size() << " (barrel = " << barrel[i] << ")" << std::endl;
    for (int j=0; j<=hits[i].size(); j++) {
      std::cout  << "\thits[" << i << "].["<<j<<"] = " << hits[i][j] << "\thits[" << i << "].at("<<j<<") = " << hits[i].at(j) << std::endl;
    }
  }

  return;
}


  
void MyVectors(void){

  std::vector <int>  my1dvector_X;
  std::vector <int>  my1dvector_Y;
  std::vector <int>  my1dvector_Z;
  std::vector< std::vector <int> > my2dvector;

  // Save 4 pixel hits per track
  for (int i=0; i < 4; i++){
    double xPos = +1.0+i;
    double yPos = -3.0+i;
    double zPos = -1.0+i;
    my1dvector_X.push_back( xPos );
    my1dvector_Y.push_back( yPos );
    my1dvector_Z.push_back( zPos );
  }


  // Fill vector with ints
  for (int i=0; i<=5; i++){
    my2dvector.push_back( std::vector<int>(i*i) );
  }
  
  // create vector iterator
  std::vector <int>::iterator it;
  std::vector <int>& innerList = my2dvector[0];
  
  it = innerList.begin(); // initialize iterator (column zero)

  std::cout << "my2dvector contains:" << std::endl;
  for ( it = innerList.end() ; it < innerList.end(); it++ ){
    // for ( it=my2dvector.begin() ; it < my2dvector.end(); it++ ){
    //cout << " (*it) = " << (*it) << endl;
    //cout << endl;
    }

return;
}

 void Precision(void){

   // float a = 1.0/7.0;
   // float a = 50.531;
   float a = 0.000531;
   
   std::cout << std::setprecision(0)  << a << std::endl;
   std::cout << std::setprecision(1)  << a << std::endl;
   std::cout << std::setprecision(2)  << a << std::endl;
   std::cout << std::setprecision(3)  << a << std::endl;
   std::cout << std::setprecision(4)  << a << std::endl;
   std::cout << std::setprecision(20) << a << std::endl;
   std::cout << std::endl;
   float b = 50.123;
   std::cout << std::setprecision(0)  << b << std::endl;
   std::cout << std::setprecision(1)  << b << std::endl;
   std::cout << std::setprecision(2)  << b << std::endl;
   std::cout << std::setprecision(3)  << b << std::endl;
   std::cout << std::setprecision(4)  << b << std::endl;
   std::cout << std::setprecision(20) << b << std::endl;

  return;
 }


// void fabs_abs(void){

//   double eta = +1.45;
//   std::cout << "+) fabs(eta) = " << fabs(eta) << ", abs(eta) = " << abs(eta) << std::endl;
//   eta  = -1.45;
//   std::cout << "-) fabs(eta) = " << fabs(eta) << ", abs(eta) = " << abs(eta) << std::endl;
  
//   return;
//}

void FindValueInVector(void)
{

  std::vector<int> pixelHits;
  pixelHits.push_back(3);
  pixelHits.push_back(3);
  pixelHits.push_back(2);
  pixelHits.push_back(1);
  pixelHits.push_back(1);
  pixelHits.push_back(-1);
  pixelHits.push_back(-1);
  pixelHits.push_back(-2);
  pixelHits.push_back(-3);

  std::cout << "here" << std::endl;
  std::vector<int>::iterator t1 = std::find (pixelHits.begin(), pixelHits.end(), 0);
  if (t1 == pixelHits.end() ) std::cout << "0 not found!" << std::endl;
  else std::cout << "0 found! It's is = " << *t1 << std::endl;

  std::vector<int>::iterator t2 = std::find (pixelHits.begin(), pixelHits.end(), 1);
  if (t2 == pixelHits.end() ) std::cout << "1 not found!" << std::endl;
  else std::cout << "1 found! It's is = " << *t2 << std::endl;
  
  return;
}

  
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
  for( std::vector<double>::iterator it = v_eta.begin(); it != v_eta.end()-1; it++){ v_binWidth.push_back( std::abs( *(it)-*(it+1) ) ); }
  
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

  return;}

void stringParse(void){

  std::string s = "Column1 & Column2 & Column3 & Column4";
  std::string delimiter = "&";
  
  size_t pos = 0;
  std::string token;
  while ((pos = s.find(delimiter)) != std::string::npos) {
    token = s.substr(0, pos);
    std::cout << token << std::endl;
    // s.erase(0, pos + delimiter.length());
    s.erase(0, pos + delimiter.length());
  }
  //  std::cout << s << std::endl;
  return;

}


int main(void){

  // double myEtaMap[] = {-2.3, -2.1, -1.9, -1.7, -1.5, -1.3, -1.1, -0.9, -0.7, -0.5, -0.3, -0.1, +0.1, +0.3, +0.5, +0.7, +0.9, +1.1, +1.3, +1.5, +1.7, +1.9, +2.1, +2.3};
  // int arrayIndex    = -1;
  // double myEtas[] = {-0.1, 0.0, 0.1};
 
  // for( int i = 0; i < 3; i++){ 
  //   arrayIndex = FindNearestIndex(24, myEtaMap, myEtas[i] ); 
  //   std::cout << "---> arrayIndex = " << arrayIndex << std::endl;
  // }
  
  // forLoop();
  // count();
  // divide();
  // booleanDeclarations();
  // eraseVectorElementAlt();
  // eraseVectorElement();
  // compareVectorElements();
  // vectorInLoop();
  // stringParse();
  // Precision();
  // FindValueInVector();
  // fabs_abs();
  // PixelAlgorithm();

  // double b = 14.2;
  // Reference(b);
  
  // MaxElement();

  // Pow();

  // MinMax();

  // AlignText();

  findTrigger();
  
  return 0;
}
