# write a python program to print the contents of a directory using os module. Search online which does that
import os

def print_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied for directory {path}.")

# Example usage
directory_path = 'MD SHAFIUL ISLAM\Downloads\Python_ChapterWise_Notes.zip\Python ChapterWise Notes\Chapter 1'  # You can change this to any directory path you want to list
print_directory_contents(directory_path)

