#main calculation function
def calculate(x, y, choice):
    try:
        if choice == '1':
            return x + y
        elif choice == '2':
            return x - y
        elif choice == '3':
            return x * y
        elif choice == '4':
            return x / y
    except ZeroDivisionError:
        return 'Cannot be divided by 0'
    
#Main Program
print('Welcome to the calculator program!')
print('Enter 1 to Add')
print('Enter 2 to substract')
print('Enter 3 to Multiply')
print('Enter 4 to Divide')
print('Enter 5 to Exit')

#loop
while True:
    try:
        choice = input("Enter choice (1,2,3,4,5): ")
        if choice not in ('1','2','3','4','5'):
            raise ValueError
    except ValueError:
        print('Invalid input, please try again!')
        continue
    
    if choice == '5':
        break
    
    while True:
        try:
            num1 = float(input('Please enter the first number: '))
            num2 = float(input('Please enter the second number: '))
            break
        except ValueError:
            print('Invalid Input. Enter numbers only.')
            continue
    
    #conditional based on user's choice
    if choice == '1':
        print(num1, '+', num2, '=', calculate(num1,num2, choice))
    elif choice == '2':
        print(num1, '-', num2, '=', calculate(num1, num2, choice))
    elif choice == '3':
        print(num1, 'x', num2, '=', calculate(num1, num2, choice))
    elif choice == '4':
        if num2 != 0:
            print(num1, '/', num2, '=', calculate(num1, num2, choice))
        else:
            print(calculate(num1, num2, choice))

    #continue or no
    choice = input('Do you want to continue? (y/n): ')
    if choice.lower() != 'y':
        break