# syntex: string.count(substring,start,end). 
# substring=A string whose occurrences it to be calculated
#start= from where to start searching(start index).defoult value is 0.its an optional
#end= where to end searching(End index). defoult is end of string.its an optional
str=input ("Enter your string: ")
count=str.count(input("Enter your searching substring: "))
print(f"your substring we find on your string {count} times")

