#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=17

digits = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten"
]

teens = digits + [
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]

specials = [
    "hundred",
    "thousand"
]


def under100(num):
    numStr = str(num)
    if num < 0:
        return ValueError("Number cannot be negative!")
    elif num < 20:
        return teens[num]
    elif num < 100:
        return tens[int(numStr[0])] + digits[int(numStr[1])]
    else:
        raise ValueError("Number must be less than 100!")


def under1000(num):
    if num < 0:
        raise ValueError("Number cannot be negative!")
    elif num < 100:
        return under100(num)
    elif num > 999:
        raise ValueError("Number must be less than 1000!")
    numStr = str(num)
    result = digits[int(numStr[0])] + specials[0]
    if numStr[1:] != "00":
        result += "and" + under100(int(numStr[1:]))
    return result


upperLimit = 1001
total = 0
for i in range(1, upperLimit):
    addition = ""
    if i < 1000:
        addition = under1000(i)
    elif i == 1000:
        addition = "one" + specials[1]
    total += len(addition)
print(total)
