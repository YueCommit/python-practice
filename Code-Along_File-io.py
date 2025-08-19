import os
# file_path = (r'data.csv')
# print(file_path)

# # absolute path
# #c://mycomputer/user/xu/documents/data.csv

# #relative path
# #data.csv

# f = open("samplefile.txt", "w")

# f.close()

# f = open("sampledata.txt", "w")
# for i in range(1,4):
#     f.write(f"{i}, row {i}, data{i+1}\r\n")
# f.close()

# f = open('sampledata.txt', "w")
# f.write("Hello World")
# sample = f.read()
# print(sample)
# f.close()

# f = open("sampledata.txt")
# sample_lines = f.readlines()
# f.close()
# print(sample_lines)

# for line in sample_lines:
#     print(line)

# os.remove("sampledata.txt")

from_user = input("Enter something: ")

f = open("samplefile.txt", "a")
f.write(from_user + "\n")
f.close()