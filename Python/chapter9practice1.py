'''write a program to read the text from a given file and find out whater it contain the word '''
st=input("Enter your string: ")
f=open(input("Enter your file name with your extention: "),"w")#here w for write form
f.write(st)
f.close()