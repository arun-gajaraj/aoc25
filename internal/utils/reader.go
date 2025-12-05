package utils

import (
	"io"
	"log"
	"os"
	"strings"
)

func ReadFileLines(path string) ([]string, error) {
	f, err := os.OpenFile("./cmd/day01/input.txt", os.O_RDONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	content, err := io.ReadAll(f)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")
	return lines, nil
}
