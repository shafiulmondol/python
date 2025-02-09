'''write  a recarsive function to calculate the sum of n first numbers'''

def sum(a):
    if(a==1):
        return 1
    return sum(a-1)+a
a=int (input("enter your number: "))
print(sum(a))