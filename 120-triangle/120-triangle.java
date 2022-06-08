class Solution {
    // without memorization
    // int n;
    // int[][] grid;
    // // rule: r >= c
    // int f(int r, int c) {
    //     if (r == n - 1)
    //         return grid[r][c];
    //     return grid[r][c] + Math.min(f(r + 1, c), f(r + 1, c + 1)); // 从现节点到最后一行的最后一行的最短距离
    // }
    // public int minimumTotal(List<List<Integer>> t) {
    //     n = t.size();
    //     grid = new int[n][n];
    //     for (int r = 0; r < n; r++)
    //         for (int c = 0; c <= r; c++)
    //             grid[r][c] = t.get(r).get(c);
    //     return f(0,0);
    // }
    
    // memorization: 加cache标准写法 | 不容易出错的标准写法
    int n;
    int[][] grid;
    int[][] dp;
    boolean[][] flag;
    // rule: r >= c
    int f(int r, int c) {
        if (flag[r][c])
            return dp[r][c];
        int val = grid[r][c];
        if (r < n - 1)
            val += Math.min(f(r + 1, c), f(r + 1, c + 1));
        dp[r][c] = val;
        flag[r][c] = true;
        return val;
    }
    
    public int minimumTotal(List<List<Integer>> t) {
        n = t.size();
        grid = new int[n][n];
        for (int r = 0; r < n; r++)
            for (int c = 0; c <= r; c++)
                grid[r][c] = t.get(r).get(c);
        dp = new int[n][n];
        flag = new boolean[n][n];
        return f(0,0);
    }
    
    
}