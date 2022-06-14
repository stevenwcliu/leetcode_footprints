class Solution {
    public int findKthPositive(int[] arr, int k) {
        
//         find an index that number of missing nums is less than k
//         想找满足条件的最大 p
//         missing of number in the range of [1, 2, 3, 4,5,...arr[p]]: < k
//             meaning missing # is > arr[p], but smaller than arr[p + 1]
            
//         [2, 3, 4, 7, 11]
//         [1, 1, 1, 3, 6] //  cnt of missing 
       
        
//         arr[p] + k - # < arr[p + 1]
//         missing of number in the range of [1...arr[p + 1]]: >= k
        
        // p is an index
        int n = arr.length, p = 0, q = n - 1;
        
        // O(1) 时间内回答arr[p] 缺的数目
        
        // 搜索范围: [p     m] [m+1      q]
        // key equation: missing # = arr[p] - (p + 1)
        
        while (p < q) {
            int mid = p + (q - p) / 2;
            // check mid + 1
            if (arr[mid + 1] - (mid + 2) < k)
                p = mid + 1;
            else
                q = mid;
        }
        // 跳出后， # of missing in [1....arr[p]] < k, p is max;
        // return arr[p] + k - (arr[p] - (p + 1)); 
        // k - (arr[p] - (p + 1))： 往后数几个
        //return k + p + 1; // 化简后
        
        // return arr[p] - (p + 1) < k ? arr[p] + k - (arr[p] - (p + 1)) : k; 
        return arr[p] - (p + 1) < k ? k + p + 1 : k; // 精简版
    }
}

