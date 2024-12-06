#include <bits/stdc++.h>
using namespace std;

signed main() {
  cin.tie(nullptr)->sync_with_stdio(false);
  vector<string> v;
  string s;
  while (cin >> s) {
    v.push_back(s);
  }

  const int n = (int)v.size();
  const int m = (int)v[0].size();

  {
    // part1

    int occur = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j + 4 <= m; j++) {
        for (auto pat : {"XMAS", "SAMX"}) {
          bool same = true;
          for (int t = 0; t < 4; t++)
            same &= v[i][j + t] == pat[t];
          if (same)
            ++occur;
        }
      }

    for (int i = 0; i + 4 <= n; i++)
      for (int j = 0; j < m; j++) {
        for (auto pat : {"XMAS", "SAMX"}) {
          bool same = true;
          for (int t = 0; t < 4; t++)
            same &= v[i + t][j] == pat[t];
          if (same)
            ++occur;
        }
      }

    for (int i = 0; i + 4 <= n; i++)
      for (int j = 0; j + 4 <= m; j++) {
        for (auto pat : {"XMAS", "SAMX"}) {
          bool same = true;
          for (int t = 0; t < 4; t++)
            same &= v[i + t][j + t] == pat[t];
          if (same)
            ++occur;
        }
      }

    for (int i = 0; i + 4 <= n; i++)
      for (int j = 3; j < m; j++) {
        for (auto pat : {"XMAS", "SAMX"}) {
          bool same = true;
          for (int t = 0; t < 4; t++)
            same &= v[i + t][j - t] == pat[t];
          if (same)
            ++occur;
        }
      }
    cout << occur << endl;
  }

  {
    // part2

    int ans = 0;
    const pair<int, int> dirs[4] = {
      {1, 1}, {1, -1}, {-1, -1}, {-1, 1}
    };

    for (int i = 1; i + 1 < n; i++)
      for (int j = 1; j + 1 < m; j++)
        if (v[i][j] == 'A') {
          string ms;
          for (auto [dx, dy] : dirs) {
            ms += v[i + dx][j + dy];
          }
          ms += ms;
          if (ms.find("MMSS") != string::npos)
            ++ans;
        }
    cout << ans << '\n';
  }
}
