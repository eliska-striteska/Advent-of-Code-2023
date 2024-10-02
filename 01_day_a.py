# Calibration document has been amended by a very young Elf who was apparently just excited to show off her art skills.
# Consequently, the Elves are having trouble reading the values on the document.
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value
# that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit
# (in that order) to form a single two-digit number.

# For example:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# Consider your entire calibration document. What is the sum of all of the calibration values?

lines = []

with open("input.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

# pouziti list comprehension:
# with open("input.txt", encoding="utf-8") as file:
#     lines = [line for line in file]


list_of_digits = []
for line in lines:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    list_of_digits.append(digits)

print(list_of_digits)

calibration_values = []
for group in list_of_digits:
    calibration_value = int(group[0] + group[-1])
    calibration_values.append(calibration_value)

#print(calibration_values)

sum_of_values = sum(calibration_values)
print(sum_of_values)
