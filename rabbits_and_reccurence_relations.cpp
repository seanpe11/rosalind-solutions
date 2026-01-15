#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;

unsigned long long int rabitt_recurrence(int n, int k){
  vector<unsigned long long int> arr(n);
  arr[0] = 1;
  arr[1] = 1;
  for(int i = 2; i < n; i++){
    arr[i] = (arr[i-1] + k * arr[i-2]);
  }
  return arr[n-1];
}

int main(){
  int n, k;
  cin >> n >> k;

  unsigned long long int ans;

  ans = rabitt_recurrence(n, k);

  cout << ans;
}
