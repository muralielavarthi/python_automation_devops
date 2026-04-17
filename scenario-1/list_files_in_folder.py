import os
import sys

# Read folder details from the user

read_folders= sys.argv[1]

# string to list
folders_list=read_folders.split(",")

for line in folders_list:
    print(line)