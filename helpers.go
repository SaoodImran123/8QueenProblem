package main

import (
	"encoding/json"
	"fmt"
	"github.com/MaxHalford/eaopt"
	"regexp"
	"strconv"
	"strings"
)

func IntegerAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func UniqueSlice(item []int, list [][]int) bool {
	for i := 0; i < len(list); i++ {
		if sliceEqual(item, list[i]) {
			return false
		}
	}
	return true
}

func sliceEqual(a []int, b []int) bool {
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

func getGnome(a eaopt.Genome) Positions {
	b, err := json.Marshal(a)
	if err != nil {
		fmt.Println(err)
		return nil
	}
	var GenomeStr = string(b)
	re, _ := regexp.Compile(`(?m)\[|\]`)
	GenomeStr = re.ReplaceAllString(GenomeStr, "")
	GenomeStrSlice := strings.Split(GenomeStr, ",")

	var genome = make(Positions, QUEEN_COUNT)
	for i, s := range GenomeStrSlice {
		genome[i], _ = strconv.Atoi(s)
	}

	return genome
}

func print2D(arr [][]int) {
	for i := 0; i < len(arr); i++ {
		line := ""
		for j := 0; j < len(arr[i]); j++ {
			line += strconv.Itoa(arr[i][j]) + " "
		}
		fmt.Println(line)
	}
}

func format1D(arr []int) string {
	line := ""
	for j := 0; j < len(arr); j++ {
		line += strconv.Itoa(arr[j]) + " "
	}
	return line
}

func format1DFloat64(arr []float64) string {
	line := ""
	for j := 0; j < len(arr); j++ {
		line += strconv.Itoa(int(arr[j])) + " "
	}
	return line
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
