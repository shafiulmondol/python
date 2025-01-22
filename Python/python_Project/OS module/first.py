import os

print(os.name)# it prints windows name
print(os.sep)# it prints \ that is uses on to any elements path
# os.makedirs("name")# it create a folder
path=os.getcwd()# it prints path of this file
print(path)
print(os.walk(path))# it visite all folder that i comand and print this folder element
for dirpaths,dirnames,filenames in os.walk(path):
    print(filenames)
