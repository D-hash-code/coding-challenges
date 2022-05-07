package main


// Leetcode 1228 https://leetcode.com/problems/missing-number-in-arithmetic-progression/
func missingNumber(arr []int) int {
    
    var gap int = arr[1] - arr[0]
    if gap == 0 {
        return arr[0]
    }
    
    if gap > 0 {
        for i:=1; i<len(arr); i++ {
            n := arr[i]
            if gap > n - arr[i-1] {
                return arr[0] + n - arr[i-1]
            }
            if gap < n - arr[i-1] {
                return arr[i-1] + gap
            }
        }
    } else {
        for i:=1; i<=len(arr); i++ {
            n := arr[i]
            if gap < n - arr[i-1] {
                return arr[0] + n - arr[i-1]
            }
            if gap > n - arr[i-1] {
                return arr[i-1] + gap
            }
        }
    }

    return 0
}
