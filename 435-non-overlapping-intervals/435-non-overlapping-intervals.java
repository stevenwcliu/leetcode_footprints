class Solution {
    int[][] ins;
    int[] dp;
    boolean[] flag;
    int f(int n) {
        if (flag[n])
            return dp[n];
        int val = 0;
        if (n > 0) {
            val = f(n - 1);
            int p = 1, q = n - 1;
            while (p < q) {
                int mid = p + (q - p) / 2;
                if (ins[mid][1] > ins[n - 1][0])
                    q = mid;
                else
                    p = mid + 1;
            }
            if (ins[p - 1][1] > ins[n - 1][0])
                p--;
            val = Math.max(val, 1 + f(p));
        }
        dp[n] = val;
        flag[n] = true;
        return val;
    }
    public int eraseOverlapIntervals(int[][] ins) {
        this.ins = ins;
        int n = ins.length;
        Arrays.sort(ins, (x, y) -> Integer.compare(x[1], y[1]));
        dp = new int[n + 1];
        flag = new boolean[n + 1];
        return n - f(n);
    }
}