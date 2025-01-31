'''write a program to mine a log file  and find out whether it contains python'''
with open("d.txt") as f:
    c=f.read()
if ("python" in c):
    print("yes")
else:
    print("no")