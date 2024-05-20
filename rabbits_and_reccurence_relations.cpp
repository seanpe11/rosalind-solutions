#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;

int main(){
  long long int n, k;
  cin >> n >> k;

  long long int ans;
  long long int a, b, c;
  a = 1;
  b = 1;
  c = k + a;

  for(int i=1;i<n;i++){
    int temp = c;
    c = a * k + b;

    a = b;
    b = temp;
  }

  cout << c;
}
