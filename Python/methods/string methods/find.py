# structure: string.find(substring,start,end); it same to index method only it invalid index return error                                
'''
substring= the substring to search for
start: Its an optional value. Default is 0. Where to start search
end: Its an optional value. Default is end of string. Where to end the search

'''
string='my name is shafiul is my education'
b=string.find('is')
print(string.find("is",10,30))
print(string.find("is",10))
print(b)
#we can find amy specific charecter or word. find method give us that specific inputs first occerance index value. If it do not find in string it print -1.