package main

import "testing"

func countPrimes(n int) int {
	ans := 0
	for i := 2; i < n; i++ {
		if isPrime(i) {
			ans += 1
		}
	}
	return ans
}

func isPrime(num int) bool {
	for i := 2; i * i <= num; i++ {
		if num % i == 0 {
			return false
		}
	}
	return true
}

func Test_countPrimes(t *testing.T)  {
	if countPrimes(0) != 0 {
		t.Errorf("Error")
	}
	if countPrimes(1) != 0 {
		t.Errorf("Error")
	}
	if countPrimes(2) != 0 {
		t.Errorf("Error")
	}
	if countPrimes(10) != 4 {
		t.Errorf("Error")
	}
}