package main

import (
	"fmt"
	"strconv"
)

func IntegerAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func UniqueSlice(item []int, list [][]int) bool {
	for i := 0; i < len(list); i++ {
		if SliceEqual(item, list[i]) {
			return false
		}
	}
	return true
}

func SliceEqual(a []int, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func Print2D(arr [][]int) {
	for i := 0; i < len(arr); i++ {
		line := ""
		for j := 0; j < len(arr[i]); j++ {
			line += strconv.Itoa(arr[i][j]) + " "
		}
		fmt.Println(line)
	}
}

func MyEval(P []int) float64 {
	var collisionCount float64 = 0

	//Ref https://stackoverflow.com/a/57374525
	for i := 0; i < len(P); i++ {
		for j := i + 1; j < len(P); j++ {

			//Check diagonal for collision
			if j-i == IntegerAbs(P[i]-P[j]) {
				collisionCount++
			}

			//Check for horizontal collision
			if P[i] == P[j] {
				collisionCount++
			}

			//Check for vertical collision
			//Not required due to 1 only 1 element allowed per column
		}
	}
	return collisionCount
}
