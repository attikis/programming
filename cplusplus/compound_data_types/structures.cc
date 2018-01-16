// structures.cc
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

struct s_Movies{
  string Title;
  int Year;
  double Rating;
} Godfather, Terminator;


// These belong to a header file!
int nMovies;
string myString;
void PrintMovie(s_Movies movies);

int main()
{

  Godfather.Title  = "The Godfather: Part I";
  Godfather.Year   = 1972;
  Godfather.Rating = 1.0;

  Terminator.Title  = "The Terminator";
  Terminator.Year   = 1984;
  Terminator.Rating = 0.7;

  cout <<  "*** My favourite movie is: " << endl;
  PrintMovie(Godfather);
  return 0;
}


void PrintMovie(s_Movies movie)
{
  cout << movie.Title;
  cout << " (Year: " << movie.Year << ", Rating: " << movie.Rating*100 << "%)\n";
}
  


  

  
