package main


// Leetcode 1134 https://leetcode.com/problems/armstrong-number/
import (
    "strconv"
    "math"
)

func isArmstrong(n int) bool {
    
    var nStr string = strconv.Itoa(n)
    var size int = len(nStr)
    var sum int
    for _, rDigit := range nStr {
        digit, _ := strconv.Atoi(string(rDigit))
        sum += int(math.Pow(float64(digit),float64(size)))
        if sum > n {
            return false
        }
    }
    if sum == n {
        return true
    }
    return false
}
