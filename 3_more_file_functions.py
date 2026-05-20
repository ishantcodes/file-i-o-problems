
f = open("file2.txt")

# read1 = f.readline()
# print(read1)

# read2 = f.readline()
# print(read2)

# read3 = f.readline()
# print(read3)

# read4 = f.readline()
# print(read4)

# read5 = f.readline()
# print(read5)

read = f.readline()
while(read != ""):                  # readline
    print(read)
    read = f.readline()


readline = f.readlines()
print(readline)                     #readlines

f.close()