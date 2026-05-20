"""
Write a program to mine a log file and find out whether it contains ‘python’.
"""

with open("log.txt") as f:
    content = f.read()
    if "python" in content or "Python" in content:
        print("\"python\" is present in the file")
    else:
        print("\"python\" is not present in the file")