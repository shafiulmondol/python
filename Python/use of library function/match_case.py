'''syntex: 
match expretion/value:
    case value 1:
        code
    case value 2:
        code
        
        
        
    case value n:
        code
    case _: (its an optional)
    ex: code=200 -page not found
        code 300 - turn over
        code 400 - thi page
    '''
code=int(input("enter your code number: "))
match code:
    case 200:
        print("page not found")
    case 300:
        print("turn over")
    case 400:
        print("this page")
    case _:
        print("invailed code number")