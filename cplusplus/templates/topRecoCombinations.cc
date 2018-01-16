// Tell the preprocessor to include iostream
// usage:
// g++ topRecoCombinations.cc -o top && ./top
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int combinations(unsigned int n, unsigned int r, string title="title")
{
  if (r > n)
    {
      throw std::invalid_argument("The value of \"r\" cannot be greater than \"n\" in nCr.");
    }
  else
    {
      // std::cout << "nCr for n = " << n << ", r = " << r << ":" << endl;
      if (0) std::cout << title << ": " << endl;
    }
  
  std::vector<bool> v(n);
  std::fill(v.begin(), v.begin() + r, true);
  unsigned int combinations=0;

  do {
       for (int i = 0; i < n; ++i)
	 {
           if (0) if (v[i]) cout << (i + 1) << " ";
	 }
       if (0) std::cout << "\n";
       combinations++;
   } while (std::prev_permutation(v.begin(), v.end()));
  
  if(0) cout << "Combinations = " << combinations << "\n" << endl;
  return combinations;
}


void test(unsigned int nJets=5)
{

  vector<int> jets;
  for (int i=0; i < nJets ; i++) jets.push_back(i);
  
  for(int i=0; i<jets.size(); i++)
    {
      
      for(int j=i+1; j<jets.size(); j++)
	{
	  
	  for(int k=i+1; k<jets.size(); k++)
	    {
	      
	      for(int l=k+1; l<jets.size(); l++)
		{
		  
		  if(  j==k || j==l) continue;

		  for(int m=k+1; m<jets.size();m++)
		    {
		      
		      for(int n=m+1; n<jets.size(); n++)
			{
			  
			  if( m==j ||  m==l || n==j  || n==l) continue;
			  std::cout << jets[i] << jets[j] << "-" << jets[k] << jets[l] <<  "-" << jets[m] << jets[n] << std::endl;
			}
		    }
		}
	    }
	}
    }
  return;
}


  void topReco(unsigned int nJets=7, unsigned int nBJets=3)
{
  // Declare variables
  vector<int> jets;
  vector<int> ljets;
  vector<int> bjets;
  int combinations = 0;
  
  // Fill vector with ints
  for (int i=0; i < nJets ; i++) jets.push_back(i);
  for (int i=0; i < nBJets; i++) bjets.push_back(i);

  // Erase bjets from
  for (int i=0; i < nJets; i++)
    {
      // std::find(jets.begin(), jets.end(), bjets.at(i)) != jets.end() jets.erase(i);
      if ( std::find(bjets.begin(), bjets.end(), jets.at(i)) != bjets.end() ) continue;
      else ljets.push_back( jets.at(i) );
    }
  

  // Inform user of event contents
  cout << "\nThere are " << ljets.size() << " light-jets: ";
  for (int i=0; i < ljets.size(); i++) cout << ljets.at(i) << " ";

  cout << "\nThere are " << bjets.size() << " bjets: ";
  for (int i=0; i < bjets.size(); i++) cout << bjets.at(i) << " ";
  cout << "\n\tj j j j b b" << endl;
  cout << "\t============" << endl;


  
  vector<int> top_jets;
  vector<int> top_bjets;
  
  // For-loop: All combinations
  for ( int i = 0; i < ljets.size(); i++)
    {

      for ( int j = i+1; j < ljets.size(); j++)
	{
	  // Ensure each jet only appears once
	  if (j==i) continue;
	  
	  for ( int k = j+1; k < ljets.size(); k++)
	    {
	      // Ensure each jet only appears once
	      if (k==i || k==j) continue;
	  
	      for ( int l = k+1; l < ljets.size(); l++)
		{
		  // Ensure each jet only appears once
		  if (l==i || l==j || l==k) continue;

		  for ( int m = 0; m < bjets.size(); m++)
		    {
		      
		      for ( int n = m+1; n < bjets.size(); n++)
			{
			  // Ensure each bjet only appears once
			  //if (n==m) continue;

			  combinations++;
			  cout << "\t" << ljets.at(i) << " " << ljets.at(j) << " " << ljets.at(k) << " " << ljets.at(l) << " " << bjets.at(m) << " " << bjets.at(n) << endl;
			  top_jets.push_back(i);
			  top_jets.push_back(j);
			  top_jets.push_back(k);
			  top_jets.push_back(l);

			  top_bjets.push_back(m);
			  top_bjets.push_back(n);

			}
		    }
		}
	    }
	}
    }
  cout << "\n\nCombinations = " << combinations << endl;

  //  GetChiSqPermutations(top_jets, top_bjets);
  
  return;
}

  void diTopCombinations(unsigned int nJets=7, unsigned int nBJets=3)
{
  // Declare variables
  vector<int> jets;
  vector<int> ljets;
  vector<int> bjets;
  vector<int> top_jet1;
  vector<int> top_jet2;
  vector<int> top_jet3;
  vector<int> top_jet4;
  vector<int> top_bjet1;
  vector<int> top_bjet2;
  int combinations = 0;
  
  // Fill vector with ints
  for (int i=0; i < nJets ; i++) jets.push_back(i);
  for (int i=0; i < nBJets; i++) bjets.push_back(i);

  // Erase bjets from
  for (int i=0; i < nJets; i++)
    {
      if ( std::find(bjets.begin(), bjets.end(), jets.at(i)) != bjets.end() ) continue;
      else ljets.push_back( jets.at(i) );
    }

  // Print the number of jets and their indices
  if (0)
    {
      cout << "\nJets = " << jets.size() << ":" << endl;
      for (int i=0; i < ljets.size(); i++) cout << ljets.at(i) << " ";
      
      // Print the number of bjets and their indices
      cout << "\nBJets = " << bjets.size() << ":" << endl;
      for (int i=0; i < bjets.size(); i++) cout << bjets.at(i) << " ";
    }

  if (1) cout << "\n=== Combinations of "<< nJets << " jets, \033[1;31m" << nBJets << " bjets:\033[0m" << endl;
  // For-loop: All combinations
  for ( int i = 0; i < ljets.size(); i++)
    {

      for ( int j = i+1; j < ljets.size(); j++)
	{
	  // Ensure each jet only appears once
	  if (j==i) continue;
	  
	  for ( int k = j+1; k < ljets.size(); k++)
	    {
	      // Ensure each jet only appears once
	      if (k==i || k==j) continue;
	  
	      for ( int l = k+1; l < ljets.size(); l++)
		{
		  // Ensure each jet only appears once
		  if (l==i || l==j || l==k) continue;

		  for ( int m = 0; m < bjets.size(); m++)
		    {
		      
		      for ( int n = m+1; n < bjets.size(); n++)
			{
			  combinations++;
			  // Save the indices
			  top_jet1.push_back(i);
			  top_jet2.push_back(j);
			  top_jet3.push_back(k);
			  top_jet4.push_back(l);
			  top_bjet1.push_back(m);
			  top_bjet2.push_back(n);

			  // Save the indices with the bjets swapped
			  top_jet1.push_back(i);
			  top_jet2.push_back(j);
			  top_jet3.push_back(k);
			  top_jet4.push_back(l);
			  top_bjet1.push_back(n);
			  top_bjet2.push_back(m);

			}// n
		    }// m
		}// l
	    }// k
	}// j
    }// i
  if (0) cout << "\n=== Combinations = " << combinations << endl;

  
  
  // reset counter
  combinations = 0;
  for ( int i = 0; i < top_bjet1.size(); i++)
    {
      // Ensure each bjet only appears once
      combinations++;
      cout << "    " << top_jet1.at(i)
	   << "  " << top_jet2.at(i)
	   << "  " << top_jet3.at(i)
	   << "  " << top_jet4.at(i)
	   << "  \033[1;31m" << top_bjet1.at(i)
	   << "  \033[1;31m" << top_bjet2.at(i)
	   << "\033[0m" << endl;
    }
  if (1) cout << "=== Combinations = " << combinations << endl;
  
  return;
}


void GetChiSqPermutations(vector<int> jets, vector<int> bjets)
{

  do {
    for (int i = 0; i < jets.size(); ++i)
      {
	cout << (i + 1) << " ";
      }
       std::cout << "\n";
  } while (std::prev_permutation(jets.begin(), jets.end()));


  return;
}


    
vector<int> GetIndices(unsigned int nJets, unsigned int nBJets)
{

  // Declare variables
  vector<int> jets;
  vector<int> ljets;
  vector<int> bjets; // vector with the indices of the b-jets (ordered in b-discriminant value)
  vector<int> indices;

  
  // Fill vector with ints
  for (int i=0; i < nJets ; i++) jets.push_back(i);
  for (int i=0; i < nBJets; i++) bjets.push_back(i);

  // Create light-jets vectir (Erase bjets from jets)
  for (int i=0; i < nJets; i++)
    {
      if ( std::find(bjets.begin(), bjets.end(), jets.at(i)) != bjets.end() ) continue;
      else ljets.push_back( jets.at(i) );
    }
  

  int combinations = 0;
  cout << "j1 j2 j3 j4 b1 b2" << endl;
  
  // bjet1
  for (int b1=0; b1 < nJets; b1++){
    // Consider only jets which are b-jets
    if ( std::find(bjets.begin(), bjets.end(), b1) == bjets.end() ) continue;

    // bjet2
    for (int b2=b1+1; b2 < nJets; b2++){
      // Consider only jets which are b-jets
      if ( std::find(bjets.begin(), bjets.end(), b2) == bjets.end() ) continue;

      // jet1
      for (int j1 = 0; j1 < nJets; j1++){
	// Ensure jet is not the same as other used jets
	if (j1 == b1 || j1 == b2) continue;

	// jet2
	for (int j2=j1+1; j2 < nJets; j2++){
	  // Ensure jet is not the same as other used jets
	  if (j2 == b1 || j2 == b2) continue;

	  // jet3 
	  for (int j3=0; j3 < nJets; j3++){
	  // Ensure jet is not the same as other used jets
	    if (j3 == b1 || j3 == b2 || j3 == j1 || j3 == j2) continue;

	    // jet4
	    for (int j4=j3+1; j4 < nJets; j4++){
	      // Ensure jet is not the same as other used jets
	      if (j4 == b1 || j4 == b2 || j4 == j1 || j4 == j2 || j4 == j3) continue;
	      
	      combinations++;
	      // cout << "b1 b2 j1 j2 j3 j4 = " << b1 << " " << b2 << " " << j1 << " " << j2 << " " << j3 << " " << j4 << endl;
	      cout << j1 << "  " << j2 << "  " << j3 << "  " << j4 << "  " << b1 << "  " << b2 << endl;

	      // TLV_W1 = TLV_jets[j1] + TLV_jets[j2];
	      // TLV_W2 = TLV_jets[j3] + TLV_jets[j4];
	      // TLV_top1 = TLV_W1 + TLV_jets[b1];
	      // TLV_top2 = TLV_W2 + TLV_jets[b2];
	      // ch2 = (TLV_W1 - MW)*(TLV_W1 - MW)/sig_W/sig_W 
	      // 	+ (TLV_W2 - MW)*(TLV_W2 - MW)/sig_W/sig_W 
	      // 	+ (TLV_top1 - TLV_top2)*(TLV_top1 - TLV_top2)/sig_dm/sig_dmt;

	      // if (ch2 < ch2min) {
	      // 	best_b1 = b1;
	      // 	best_b2 = b2; 
	      // 	best_j1 = j1;
	      // 	best_j2 = j2; 
	      // 	best_j3 = j3;
	      // 	best_j4 = j4;
	      // }
	      
	    }
	  }
	}
      }
    }
  }

  // vector<int> W1cont, W2cont, indices;
  // w1cont.push_back(best_j1);
  // w1cont.push_back(best_j2);
  // w2cont.push_back(best_j3);
  // w2cont.push_back(best_j4);
  // for (k=0; k<njets; k++){
  //   if (k == best_b1) indices.push_back(1);
  //   else if (k == best_b2) indices.push_back(-1);
  //   else if (find(W1cont.begin(),W1cont.end(), k)!=W1cont.end()) indices.push_back(2);
  //   else if (find(W2cont.begin(),W2cont.end(),k)!=W2cont.end())indices.push_back(-2);
  //   else indices.push_back( 0 );
  // }
  cout << "\nCombinations = " << combinations << endl;
  return indices;  
}


int topRecoCombinations(unsigned int nJets = 6, unsigned int nBJets = 2)
{

  unsigned int nLJets = nJets-nBJets;
  int combinations_ljetSelection = combinations(nLJets, 4, "jet-selection (l-jets)");
  int combinations_bjetSelection = combinations(nBJets, 2, "jet-selection (b-jets)");
  int combinations_chiSqr        = combinations(4, 2, "chiSqr (jets)") * combinations(2, 1, "chiSqr (b-jets)");
  int combinations = combinations_ljetSelection * combinations_bjetSelection * combinations_chiSqr;
  cout << "=== Combinations = " << "ljetSelection x bjetSelection x chiSqr = " << combinations_ljetSelection << " x " << combinations_bjetSelection << " x " << combinations_chiSqr << " = " << combinations << endl;
  
  return combinations;
}

  
// main function declaration 
int main() {

  // Works
  // diTopCombinations(6, 2);
  diTopCombinations(7, 3);
  diTopCombinations(8, 3);
  // diTopCombinations(8, 4);
  // diTopCombinations(9, 4);
  // diTopCombinations(9, 5);
  // diTopCombinations(11, 3);

  // Testing
  // topRecoCombinations(6, 2);
  // topRecoCombinations(8, 4);
  // topRecoCombinations(8, 3);
  // test(7);
  // topReco(7, 3);
  // topReco(6, 2);
  // vector<int> indices = GetIndices(6, 2);

  return 0;
}
