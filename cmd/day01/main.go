package main

import (
	"fmt"
	"strconv"

	"github.com/arun-gajraj/aoc2025/internal/utils"
)

func main() {

	input, err := utils.ReadFileLines("cmd/day01/input.txt")
	if err != nil {
		panic(err)
	}

	pos := 50
	zeros := 0

	for _, line := range input {

		dir := line[:1]
		num := line[1:]
		turns, _ := strconv.Atoi(num)
		delta := 1

		if dir == "L" {
			delta = -1
		}

		for range turns {
			pos += delta

			pos %= 100
			if pos < 0 {
				pos += 100
			}

		}
		if pos == 0 {
			zeros += 1
		}

	}

	fmt.Println("number of zeros is : ", zeros)

	part2()
}

func part2() {
	input, err := utils.ReadFileLines("cmd/day01/input.txt")
	if err != nil {
		panic(err)
	}

	pos := 50
	zeros := 0

	for _, line := range input {

		dir := line[:1]
		num := line[1:]
		turns, _ := strconv.Atoi(num)
		delta := 1

		if dir == "L" {
			delta = -1
		}

		for range turns {
			pos += delta

			pos %= 100
			if pos < 0 {
				pos += 100
			}

			if pos == 0 {
				zeros += 1
			}

		}

	}

	fmt.Println("Part 2 zeros: ", zeros)

}
