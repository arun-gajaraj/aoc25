package main

import (
	"fmt"
	"os"

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

	part1()
}

func part1() {}
