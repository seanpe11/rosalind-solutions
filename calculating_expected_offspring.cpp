#include <iostream>
#include <string>
using namespace std;

int main() {
  int AAAA_count = 0, AAAa_count = 0, AAaa_count = 0, AaAa_count = 0,
      Aaaa_count = 0, aaaa_count = 0;

  cin >> AAAA_count;
  cin >> AAAa_count;
  cin >> AAaa_count;
  cin >> AaAa_count;
  cin >> Aaaa_count;
  cin >> aaaa_count;

  float dominant_prob = 0;
  dominant_prob += 1.0 * AAAA_count * 2;
  dominant_prob += 1.0 * AAAa_count * 2;
  dominant_prob += 1.0 * AAaa_count * 2;
  dominant_prob += 0.75 * AaAa_count * 2;
  dominant_prob += 0.50 * Aaaa_count * 2;
  dominant_prob += 0 * aaaa_count * 2;

  cout << dominant_prob << endl;

  return 0;
}
