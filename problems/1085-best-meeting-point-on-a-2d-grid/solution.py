def best_meeting_point(grid):
    # grid is a list of lists containing 0s and 1s
    # return the minimum total Manhattan distance as an int
    rows = []
    cols = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                rows.append(i)
                cols.append(j)
    if not rows:
        return 0
    def median(values):
        n = len(values)
        if len(values) % 2 == 1:
            return values[n // 2]
        else:
            return (values[(n // 2) - 1] + values[n // 2]) // 2
    best_row = median(rows)
    best_col = median(sorted(cols))
    min_distance_md = 0.0
    for x, y in zip(rows, cols):
        min_distance_md += (abs(x - best_row) + abs(y - best_col))
    return min_distance_md


# #include <bits/stdc++.h>
# using namespace std;
# int best_meeting_point(vector<vector<int>>& grid) {
#     int m = grid.size();
#     int n = grid[0].size();
#     vector<pair<int,int>> homes;
#     for (int r = 0; r < m; r++) {
#         for (int c = 0; c < n; c++) {
#             if (grid[r][c] == 1)
#                 homes.push_back({r, c});
#         }
#     }
#     if (homes.empty()) return 0;
#     int ans = INT_MAX;
#     for (int targetR = 0; targetR < m; targetR++) {
#         for (int targetC = 0; targetC < n; targetC++) {
#             vector<vector<int>> dist(m, vector<int>(n, 1e9));
#             dist[targetR][targetC] = 0;
#             bool changed = true;
#             while (changed) {
#                 changed = false;
#                 // forward sweep
#                 for (int r = 0; r < m; r++) {
#                     for (int c = 0; c < n; c++) {
#                         int old = dist[r][c];
#                         if (r > 0)
#                             dist[r][c] = min(dist[r][c], dist[r-1][c] + 1);
#                         if (c > 0)
#                             dist[r][c] = min(dist[r][c], dist[r][c-1] + 1);
#                         if (dist[r][c] != old) changed = true;
#                     }
#                 }
#                 // backward sweep
#                 for (int r = m-1; r >= 0; r--) {
#                     for (int c = n-1; c >= 0; c--) {
#                         int old = dist[r][c];
#                         if (r + 1 < m)
#                             dist[r][c] = min(dist[r][c], dist[r+1][c] + 1);
#                         if (c + 1 < n)
#                             dist[r][c] = min(dist[r][c], dist[r][c+1] + 1);
#                         if (dist[r][c] != old) changed = true;
#                     }
#                 }
#             }
#         }
#     }
# }