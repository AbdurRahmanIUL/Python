# By using of AI :Write a python program to print the contents of a  directory using the os module.
#search online for the function which does that.

import os  #os is built in module

# Specify the directory you want to list
directory = "."  #yaha jis folder me janna hai kon file hai waha ki directory copy kar dena

try:
    # Get list of files and folders
    contents = os.listdir(directory)
    
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: Directory '{directory}' not found.")
except PermissionError:
    print(f"Error: No permission to access '{directory}'.")


