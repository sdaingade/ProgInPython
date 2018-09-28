import os

def rename_files():
    os.chdir("C:\Swapnil\ProgInPython\prank\prank")
    
    #1. Get the files names from a folder
    file_list = os.listdir(".")
    print(file_list)
    #2. for each file, rename the filename
    for filename in file_list:
        new_name = filename.translate(None, "0123456789")
        print("Renaming " + filename + " to " + new_name)
        os.rename(filename, new_name)
        
rename_files()
