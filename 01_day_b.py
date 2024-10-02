# It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight,
# and nine also count as valid "digits".
# You now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

import re

lines = []

with open("input.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

# Nahrazení slov číslicemi

replace_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# list STR cislic
list_digit_str = replace_dict.keys()

# list vysledku
list_digit = []

for line in lines:
    line_list_digit = []
    # loop pres vsechny charaktery radku
    # funkce enumerate(iterable, start=0)
    for index, char in enumerate(line):
        # pokud je charakter cislice, uloz ji
        if char.isdigit():
            line_list_digit.append(char)
        # pokud je charakter string, loop, ktery otestuje zda zacina na nekterou cislici z replace_dict
        else:
            for digit_str in list_digit_str:
                if bool(re.match(digit_str, line[index:])):
                    line_list_digit.append(digit_str)
    list_digit.append(line_list_digit)
# print(list_digit)

only_digit_lines = []
for line in list_digit:
    new_line = " ".join(line)
    for key, value in replace_dict.items():
        pattern = re.compile(rf"{key}")
        new_line = pattern.sub(value, new_line)
    only_digit_lines.append(new_line.split())

# print(only_digit_lines)

calibration_values = []
for group in only_digit_lines:
    calibration_value = int(group[0] + group[-1])
    calibration_values.append(calibration_value)

print(calibration_values)

sum_of_values = sum(calibration_values)
print(sum_of_values)
