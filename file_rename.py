"""
Rename files from a folder

Get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip

"""

import os

directory = r"C:\Users\shandracorbitt\Desktop\ShandraBates_Python\prankOrig"

def rename_files():
    """
    Create a function to rename files in a folder
    :return: nothing
    """
    files = os.listdir(directory)
    saved_path = os.getcwd()   # save current directory
    # Go to the files' directory
    os.chdir(directory)
    for file in files:
        #remove digits from name
        new_file = file.lstrip("0123456789")
        print("old name", file, "new name", new_file)
        #rename file to new name
        os.rename(file, new_file)
    # Get back to original directory
    os.chdir(saved_path)


def main():
    """
    Test function
    :return: nothing
    """
    rename_files()


if __name__ == '__main__':
    main()
    exit(0)

