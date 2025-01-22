'''read any txt file '''
f=open(input("Enter your file name with extention: "))
data=f.read()
print(data)
f.close()
'''write any file'''
st="my name is shafiul i am a student"
my=open("dx.txt","w")# its create a new new file according to your extention 
my.write(st)# you can write any string on that file 
#my.write(input("Enter your string: "))
my.close()