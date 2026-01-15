#include <iostream>
#include <map>
#include <string>
using namespace std;

map<string, string> codonMap = {
    // Col 1
    {"UUU", "F"},
    {"UUC", "F"},
    {"UUA", "L"},
    {"UUG", "L"},
    {"UCU", "S"},
    {"UCC", "S"},
    {"UCA", "S"},
    {"UCG", "S"},
    {"UAU", "Y"},
    {"UAC", "Y"},
    {"UAA", "Stop"},
    {"UAG", "Stop"},
    {"UGU", "C"},
    {"UGC", "C"},
    {"UGA", "Stop"},
    {"UGG", "W"},

    // Col 2
    {"CUU", "L"},
    {"CUC", "L"},
    {"CUA", "L"},
    {"CUG", "L"},
    {"CCU", "P"},
    {"CCC", "P"},
    {"CCA", "P"},
    {"CCG", "P"},
    {"CAU", "H"},
    {"CAC", "H"},
    {"CAA", "Q"},
    {"CAG", "Q"},
    {"CGU", "R"},
    {"CGC", "R"},
    {"CGA", "R"},
    {"CGG", "R"},

    // Col 3
    {"AUU", "I"},
    {"AUC", "I"},
    {"AUA", "I"},
    {"AUG", "M"},
    {"ACU", "T"},
    {"ACC", "T"},
    {"ACA", "T"},
    {"ACG", "T"},
    {"AAU", "N"},
    {"AAC", "N"},
    {"AAA", "K"},
    {"AAG", "K"},
    {"AGU", "S"},
    {"AGC", "S"},
    {"AGA", "R"},
    {"AGG", "R"},

    // Col 4
    {"GUU", "V"},
    {"GUC", "V"},
    {"GUA", "V"},
    {"GUG", "V"},
    {"GCU", "A"},
    {"GCC", "A"},
    {"GCA", "A"},
    {"GCG", "A"},
    {"GAU", "D"},
    {"GAC", "D"},
    {"GAA", "E"},
    {"GAG", "E"},
    {"GGU", "G"},
    {"GGC", "G"},
    {"GGA", "G"},
    {"GGG", "G"}

};

int main() {
  string s;
  cin >> s;
  string coded = "";
  for (int i = 0; i < s.length(); i += 3) {
    cout << (s.substr(i, 3)) << endl;
    coded += codonMap[s.substr(i, 3)];
  }
  cout << coded << endl;
  return 0;
}
