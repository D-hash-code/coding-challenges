package main

// Leetcode 1056 https://leetcode.com/problems/confusing-number/
import (
    "strconv"
    "strings"
    "fmt"
)

func confusingNumber(n int) bool {
    // iterate through digits
        // map digit to new digit, 
        // if digit is invalid return false
    // if new digit is different return true else false
    
    var inputNumber string = strconv.Itoa(n)
    var outputNumber string
    var iterDigit string
    
    const invalid, validSame, six, nine string = "23457", "018", "6", "9"
    
    for _, runeDigit := range inputNumber {
        digit := string(runeDigit)
        if strings.Contains(invalid,digit) {
            return false
        } else if strings.Contains(validSame,digit) {
            iterDigit = digit
        } else if digit == six {
            iterDigit = nine
        } else if digit == nine {
            iterDigit = six
        }
        outputNumber = iterDigit + outputNumber
    }
    
    if outputNumber != inputNumber {
        return true
    }
    return false
}
