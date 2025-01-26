"""write a program to find out wheter a given post is taking about 'shafiul' or not"""
a=input("Enter your post: ")
if ("shafiul".lower() in a.lower()):
    print("this post is talking about shafiul")
else:
    print("this post is not talking about shafiul")