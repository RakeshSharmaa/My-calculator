
print('welcome to the calculator')
a = int(input('Enter your first no = '))
c = input('Enter +,-,/ or * = ')
b = int(input('Enter your second no = '))
if (c == '+') :
    print('your add is = ', a+b)
elif (c == '-') :
    print('your sub is = ', a-b)
elif (c == '/') :
    print('your div is = ', a/b)
elif (c == '*') :
    print('your multi is = ', a*b)
else :
    print('Oops something went wrong try again !!')
