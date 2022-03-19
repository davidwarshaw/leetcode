#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the timeInWords function below.
def timeInWords(h, m):

    number_words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"
    ]
    if m > 30:
        hour_word = number_words[(h + 1) % 12]
        adjusted_m = 60 - m
        connector = ' to '
    else:
        hour_word = number_words[h]
        adjusted_m = m
        connector = ' past '

    minute_word = number_words[adjusted_m]
    if m == 1:
        minute_word += ' minute'
    else:
        minute_word += ' minutes'

    o_clock = ""
    if adjusted_m == 30:
        minute_word = "half"
    if adjusted_m == 15:
        minute_word = "quarter"
    elif adjusted_m == 0:
        minute_word = ""
        connector = ""
        o_clock = "o' clock"

    return minute_word + connector + hour_word + o_clock

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
