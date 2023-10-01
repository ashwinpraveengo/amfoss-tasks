package main

import (
	"fmt"
)

func Prime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	for i := 5; float64(i)*float64(i) <= float64(n); i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func main() {
	var N int
	fmt.Print("Enter a value for N: ")
	_, err := fmt.Scanf("%d", &N)
	if err != nil || N <= 1 {
		fmt.Println("Invalid input. N must be greater than 1.")
		return
	}

	fmt.Printf("Prime numbers up to %d are:\n", N)
	for i := 2; i <= N; i++ {
		if Prime(i) {
			fmt.Printf("%d ", i)
		}
	}
	fmt.Println()
}
