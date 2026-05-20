# f = open("file1.txt")
# file = f.read()
# print(file)

# f.close() 

# USING "WITH" METHOD WE DONT HAVE TO CLOSE THE FILE 

with open("file1.txt") as f:
    print(f.read())