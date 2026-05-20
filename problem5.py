"""
Repeat program 4 for a list of such words to be censored.
"""

l = ["bad", "ugly", "fool", "nonsense" , "Donkey", "stupid", "idiot"]

with open("file2.txt", "r") as f:
    content = f.read()
    for word in l:
        if word in content:
            content = content.replace(word, "#####")
         
with open("file2.txt","w") as f:
    f.write(content)