'''write a programe to multiplication table fron 2 to 20 and write it to 
the different files and place this file in a folder for 13 years old child'''
for i in range(2,4):
    j=1
    while(j!=11):
        w=(f"{i} X {j} = {i*j}\n")
        f=open(f"{i}_multi.txt","a")
        f.write(w)
        j+=1
f.close()