package main

// Leetcode 1180 https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/


func getArithmeticSum(n int) int {
    return int(n*(n+1)/2)
}

func countLetters(s string) int {
    
    var currLetter string = string(s[0])
    var substringLength int
    var out int
    
    for _, letter := range s {
        if string(letter) == currLetter {
            substringLength++
        } else {
            out += getArithmeticSum(substringLength)
            substringLength = 1
            currLetter = string(letter)
        }
    }
    
    return out + getArithmeticSum(substringLength)
}   
