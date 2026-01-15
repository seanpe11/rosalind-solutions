#include <iostream>
#include <string>
using namespace std;

int main() {
  string s1, s2;
  cin >> s1;
  cin >> s2;
  int distance = 0;

  for (int i = 0; i < s1.length(); i++) {
    if (s1[i] != s2[i]) {
      distance++;
    }
  }
  cout << distance << endl;
  return 0;
}
