"""
Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
"""

f = open("file1.txt")

content = f.read()

if "Twinkle" in content or "twinkle" in content:
    print("The word \"Twinkle\" is present in this file")
else:
    print("The word \"Twinkle\" isn't present in this file")

    f.close()