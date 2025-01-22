# this method breaks up a string at specified separetor and returns a list of string 
# syntex:- string.split(separator,maxsplit)
#separator:- separator for splitting string.Bydefault whitespace is a separator 
# maxsplit:- how many splits to do 
string1='my name is shafiul mondol'
name=string1.split()
print(len(name))
print(name)
string2='bd,india,cina,banf,kjhj'
con=string2.split(',')
print(len(con))
print(con)
country=string2.split(',',3)
print(len(country))
print(country)