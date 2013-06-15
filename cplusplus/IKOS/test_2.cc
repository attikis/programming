// test_2.cc
#include <iostream>
#include <vector>
using namespace std;

class Portfolio{

private:
  string pName;
  int nUnits;
  vector<string> v_StockName;
  vector<double> v_StockPrice;
  vector<string> v_StockCurrency;
  string * a_StockName;   // dynamic array declaration
  double * a_StockPrice;  // dynamic array declaration
  string * a_StockCurrency;  // dynamic array declaration
public:
  // Constructors/Destructors
  Portfolio(); 
  Portfolio(string name, int units);
  ~Portfolio();
  
  // Functions
  void PrintPName(void){cout << "*** " << pName << " Portfolio  ***" << endl;};
  void PrintVectors(void);
  void PrintArrays(void);
  void InitVectors(void);
  void InitArrays(void);
  void SetNamePriceCurrency(int number, string name, double price, string myCurrency = " $");

};

Portfolio::Portfolio(string name, int units){
  pName = name; 
  nUnits = units;
  InitVectors();
  InitArrays();
}


Portfolio::~Portfolio(){
  
  pName = "none";
  nUnits = -1;

  v_StockName.clear();
  v_StockPrice.clear();
  v_StockCurrency.clear();

  delete [] a_StockName;
  delete [] a_StockPrice;
  delete [] a_StockCurrency;
  
}
    
void Portfolio::InitVectors(void){
  // Set Minimum capacity for the vector to nUnits.
  v_StockName.reserve(nUnits);
  v_StockPrice.reserve(nUnits);

  for (int i = 0; i < nUnits; i++){
    v_StockName.push_back("none");
    v_StockPrice.push_back(-1.0);
    v_StockCurrency.push_back("none");
  }
  
    return;
  }
 
  
void Portfolio::InitArrays(void){

  a_StockName     = new string[nUnits];  // dynamic array creation
  a_StockPrice    = new double[nUnits];  // dynamic array creation
  a_StockCurrency = new string[nUnits];  // dynamic array creation

   // Initialise arrays
   for (int i=0; i < nUnits; i++){

     a_StockName[i] = "none";
     a_StockPrice[i] = -1.0;
     a_StockCurrency[i] = "none";
   }
   return;
 }

void Portfolio::PrintVectors(void){

  vector<string>::iterator it_StockName;
  vector<double>::iterator it_StockPrice = v_StockPrice.begin();
  vector<string>::iterator it_StockCurrency = v_StockCurrency.begin();

  cout << "\n *** Stock Name | Price | Currency (vector)" << endl;
  for (it_StockName = v_StockName.begin(); it_StockName < v_StockName.end(); it_StockName++){

    cout << (*it_StockName) << "  " << (*it_StockPrice) <<  "  " << (*it_StockCurrency) << endl;
    it_StockCurrency++;
    it_StockPrice++;
  }

  return;
}

void Portfolio::PrintArrays(void){

  cout << "\n *** Stock Name | Price | Currency (array)" << endl;
  for (int i=0; i < nUnits; i++){
    cout << a_StockName[i] << "  " << a_StockPrice[i] << "  " << a_StockCurrency[i] << endl;
  }
  
  return;
}

void Portfolio::SetNamePriceCurrency(int number, string name, double price, string myCurrency){
  a_StockName[number]     = name;
  a_StockPrice[number]    = price;
  a_StockCurrency[number] = myCurrency;

  v_StockName[number]     = name;
  v_StockPrice[number]    = price;
  v_StockCurrency[number] = myCurrency;
  
  return;
}
  


int main(void){

  Portfolio IKOS("IKOS", 10);
  IKOS.PrintPName();

  IKOS.SetNamePriceCurrency(0, "APPLE", 99.10, "JPY");
  IKOS.SetNamePriceCurrency(1, "MICROSOFT", 81.23, "GBP");
  IKOS.SetNamePriceCurrency(2, "ACER", 19.12, "USD");
  IKOS.SetNamePriceCurrency(3, "TOSHIBA", 39.45, "CHF");
  IKOS.SetNamePriceCurrency(4, "HP", 42.51, "EUR");
  IKOS.SetNamePriceCurrency(5, "IBM", 90.91, "GBP");
  IKOS.SetNamePriceCurrency(6, "NEXUS", 21.20, "EUR");
  IKOS.SetNamePriceCurrency(7, "GOOGLE", 59.04, "GBP");
  IKOS.SetNamePriceCurrency(8, "PACKARD-BELL", 32.82, "JPY");
  IKOS.SetNamePriceCurrency(9, "DELL", 55.91, "CHF");

  IKOS.PrintArrays();
  IKOS.PrintVectors();

  return 0;

}
