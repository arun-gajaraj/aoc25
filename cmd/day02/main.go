package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/arun-gajraj/aoc2025/internal/utils"
)

var input []string

func main() {

	var err error
	inputFile := os.Args[1]

	input, err = utils.ReadFileLines(fmt.Sprintf("./%s", inputFile))
	if err != nil {
		panic(err)
	}

	ranges := strings.Split(input[0], ",")

	part1(ranges)
}

func part1(ranges []string) {

	for _, sv := range ranges {

		ns := strings.Split(sv, "-")

		begin, _ := strconv.Atoi(ns[0])
		end, _ := strconv.Atoi(ns[1])

		for i := begin; i <= end; i += 1 {

		}

	}
}
