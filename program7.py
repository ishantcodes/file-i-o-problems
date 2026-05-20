"""
Write a program to find out the line number where python is present from ques 6.
"""

with open("log.txt") as f:

    lines = f.readlines()

line_no = 1

for line in lines:

    if "python" in line or "Python" in line:

        print(f'"python" is present on line number {line_no}')

    line_no += 1