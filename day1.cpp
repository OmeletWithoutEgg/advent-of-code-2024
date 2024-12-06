#include <bits/stdc++.h>
using namespace std;

signed main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  int a, b;
  vector<int> u, v;
  while (cin >> a >> b) {
    u.push_back(a);
    v.push_back(b);
  }
  ranges::sort(v);

  int64_t ans = 0;
  for (int x : u) {
    auto [l, r] = ranges::equal_range(v, x);
    ans += x * (r - l);
  }
  cout << ans << '\n';
}
