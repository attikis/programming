// binomial.cpp

// Include the libraries needed for the preprocessor
#include <iostream> // needed for cin, cout. 
#include <cmath> // need for advanced math calculations like pow(x,y) = x^{y}

// Use the standard library namespace
using namespace std;

// Declare my class here
class Binomial{
private:
  float p, q;
  int n;
public:
  Binomial(int nTrials, float probability);
  ~Binomial();
  int Factorial(int num);
  int GetBinomialCoefficient(int k);
  float GetProbability(int k);
  float GetCumulativeProbability(int k, string logicSymbol);
};

// The Constructor: Automatically called whenever a new object of this class is created. 
// Has no return value
Binomial::Binomial(int nTrials, float probability){
  n = nTrials;
  p = probability;
  q = 1-p; 
}

// The Destructor: Automaticall called when an object is destroyed. This might happen if the object's scope of existence
// has finished (e.g. defined within a function and the function ends) or it is released using the operator delete (e.g. delete object;). 
// Has no return value
Binomial::~Binomial(){};

// Define a function that calculates the factorial of a int integer data type. Use int for better precision.
int Binomial::Factorial(int num){
  
  if (num > 1){
    int value = num*Factorial(num-1);
  return value;
  }
  else{
    int value = 1;
  return value;
  }
}

// Define a function that calculates the binomial coefficient nCk for "k" successes.
int Binomial::GetBinomialCoefficient(int k){

  // cout << "*** Calculating Binomial Coefficient nCk = " << n << "C" << k << " = " << n << "!/[" << "(" << n << " - " << k << ")! " << k << "!]" << endl;
  int nCk = Factorial(n)/(Factorial(n-k)*Factorial(k));

  return nCk;
}

// Define a function that calculates the binomial coefficient nCk for "k" successes.
float Binomial::GetProbability(int k){

  // cout << "\n*** Calculating Binomial Probability for k = " << nSuccesses << " for Binomial with parameters (n, p) = (" << n << ", " << p << ")" << endl;  
  // Sanity check
  if (k>n){
    cout << "ERROR! Something went wrong as k>n. Returning -1.0" << endl;
    return -1.0;
  }
  
  int nCk = GetBinomialCoefficient(k); // no need to use an object to call a class function within the very same class!
  float probability = nCk * pow(p, k) * pow(q, n-k);
  
  // cout << "P(X = " << k << ") = " << p << endl;

  return probability;
}

// Define a function that calculates the binomial coefficient nCk for "k" successes.
float Binomial::GetCumulativeProbability(int k, string rangeSymbol){

  // cout << "*** Calculating Cumulative Binomial Probability for k >= " << nSuccesses << " for Binomial with parameters (n, p) = (" << n << ", " << p << ")" << endl;  
  float p = 0.0;
  int rangeSymbolCode = 0;
  if (rangeSymbol == "="){ rangeSymbolCode = 0;}
  else if (rangeSymbol == ">="){ rangeSymbolCode = 1;}
  else if (rangeSymbol == ">"){ rangeSymbolCode = 2;}
  else if (rangeSymbol == "<="){ rangeSymbolCode = 3;}
  else if (rangeSymbol == "<"){ rangeSymbolCode = 4;}
  else{
    cout << "ERROR! Unrecognised range symbol " << rangeSymbol << ". Returning p = -1.0" << endl;
  }
  
  // NOTE! Switch can only take int, char and enum as argument. So you cannot use a string!
  switch (rangeSymbolCode){
  case 0:
    p = GetProbability(k);
    break;
  case 1:
    for (int i=k; i <=n; i++){
      p = p + GetProbability(i);
    }
    break;
  case 2:
    for (int i=k+1; i <=n; i++){
      p = p + GetProbability(i);
    }
    break;
  case 3:
    for (int i=k; i >=0; i--){
      p = p + GetProbability(i);
    }
    break;
  case 4:
    for (int i=k-1; i >=0; i--){
      p = p + GetProbability(i);
    }
    break;
  default:
    cout << "ERROR! Unrecognised logic symbol. Returning p = -1.0" << endl;
  }
  
  cout << "P(X " << rangeSymbol << " " << k << " ) = " << p << endl;
  return p;
}

// Define the main function here.
int main(void){
  
  // Create an object of class-type Binomial. The Constructor demands two parameters to be defined at declaration time: number of trials "n" and binomial probability "p"
  int k   = 2;
  int n   = 3;
  float p = 0.5;
  float pTotal;

  // Create a new object of type Binomial. Requires two parameters: n and p.
  Binomial MyBinomial(3, 0.5);
  pTotal = MyBinomial.GetCumulativeProbability(k, "=");
  pTotal = MyBinomial.GetCumulativeProbability(k, "<");
  pTotal = MyBinomial.GetCumulativeProbability(k, "<=");
  pTotal = MyBinomial.GetCumulativeProbability(k, ">");
  pTotal = MyBinomial.GetCumulativeProbability(k, ">=");

  return 0;
}
