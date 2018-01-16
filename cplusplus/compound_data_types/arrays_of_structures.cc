// arrays_of_structures.cc
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

#define N_MOVIES 3

struct s_movies{
  string title;
  int year;
} films [N_MOVIES];

void PrintMovie (s_movies movie);

int main(){

  string myString;
  int n;

  for(n=0; n<N_MOVIES; n++){

    cout << "*** Enter title: ";
    getline(cin, films[n].title);

    cout << "*** Enter year: ";
    // getline(cin, films[n].year); will also work
    getline(cin, myString);
    stringstream(myString) >> films[n].year;
  }
  
  cout << "*** You have entered these movies: " << endl;

  for(n=0; n<N_MOVIES; n++){

    PrintMovie(films[n]);
  }

  return 0;
}

  void PrintMovie (s_movies movie){
    cout << movie.title << "( " << movie.year << ")\n" ;
  }


