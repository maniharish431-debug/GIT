import os
import subprocess

# Define the full path
file_path = "C:\\Users\\91900\\Documents\\GIT\\Python_scripts\\test.txt"
dir_path = "C:\\Users\\91900\\Documents\\GIT\\Python_scripts\\"

if os.path.exists(file_path):
    print("Writing to the file")
    with open (file_path,"w+") as f:
        f.write("Summa5")
        f.seek(0)
        lines=f.readlines()
        print(lines)

else:
    print("File not exists")

print("End of program!!")
print("End of program by mani harish")
