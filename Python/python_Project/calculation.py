while True:
    n1=int(input("Enter your first number: "))
    n2=int(input ('Enter second number: '))
    choice=input('''Choice your operation:
         1. Addition.
         2. Substraction
         3. Multiplication
         4. Division:
    choice from above:  ''')
    if choice=='1':
        print(f'Addition is {n1+n2}')
    elif choice=='2':
        print(f'Substraction is {n1-n2}')
    elif choice=='3':
        print(f'Multiplication is {n1*n2}')
    elif choice=='4':
        print(f'Division is {n1/n2}')
    else:
        print('please enter above one. ')
    disition=input('do you want to continue? y/n :  ')
    b=disition.lower()
    if b=='y':
        continue
    else:
        break


