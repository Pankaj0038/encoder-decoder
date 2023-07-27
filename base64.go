package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func binary(num int) string {
	var init string
	for num > 0 {
		var i int = num % 2
		val := strconv.Itoa(i)
		init += val
		num = num / 2
	}
	var result string
	for _, char := range init {
		result = string(char) + result
	}
	var l int = len(result)
	var y int = 8 - l
	if y != 0 {
		for y > 0 {
			result = string("0") + result
			y--
		}
	}
	return result
}
func debinary(num int) string {
	var init string
	for num > 0 {
		var i int = num % 2
		val := strconv.Itoa(i)
		init += val
		num = num / 2
	}
	var result string
	for _, char := range init {
		result = string(char) + result
	}
	var l int = len(result)
	var y int = 6 - l
	if y != 0 {
		for y > 0 {
			result = string("0") + result
			y--
		}
	}
	return result
}
func ascii(char rune) int {
	var val int = int(char)
	return val
}
func chunks(str string) []string {
	var x int = len(str) % 6
	for x > 0 {
		str += string("0")
		x--
	}
	var chunk = []string{}
	for i := 0; i < len(str)-6; i = i + 6 {
		chunk = append(chunk, str[i:i+6])
	}
	return chunk
}
func bintoint(chunks []string) []int64 {
	var x = []int64{}
	for _, i := range chunks {
		var y int64
		y, _ = strconv.ParseInt(i, 2, 8)
		x = append(x, y)
	}
	return x
}
func encode(chunks []int64) string {
	var arr string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	var ans string
	for _, i := range chunks {
		ans += string(arr[i])
	}
	return ans
}
func dechunks(str string) []string {
	var x int = len(str) % 8
	for x > 0 {
		str += string("0")
		x--
	}
	var chunk = []string{}
	for i := 0; i < len(str)-8; i = i + 8 {
		chunk = append(chunk, str[i:i+8])
	}
	return chunk
}
func findIndex(enc string) []int {
	var arr string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	index := []int{}
	for _, char := range enc {
		for i := range arr {
			if rune(arr[i]) == char {
				index = append(index, i)
			}
		}
	}
	return index
}
func decode(enc []int64) string {
	var str string
	for _, char := range enc {
		str += string(char)
	}
	return str
}
func main() {
	fmt.Printf("Enter the string to encode or decode : ")
	reader := bufio.NewReader(os.Stdin)
	inp, _ := reader.ReadString('\n')
	fmt.Printf("Enter 0 for encode and 1 for decode :")
	input := bufio.NewReader(os.Stdin)
	choose, _ := input.ReadString('\n')
	choice := strings.TrimSpace(choose)
	switch choice {
	case "0":
		var str string
		for _, i := range inp {
			str += binary(ascii(i))
		}
		var c []string = chunks(str)
		var x []int64 = bintoint(c)
		enc := encode(x)
		fmt.Println("The encoded string : ", enc)
	case "1":
		x := findIndex(inp)
		fmt.Println(x)
		var str string
		for i := range x {
			str += debinary(x[i])
		}
		fmt.Println(str)
		y := dechunks(str)
		fmt.Println(y)
		z := bintoint(y)
		fmt.Println(z)
		fmt.Println(decode(z))
	}
}
