number=int(input('Enter the number to generate Fibonacci series : '))
sum = 0
x = 1
while number > 0:
    sum,x = x,sum+x
    number -= 1
    print(x)
