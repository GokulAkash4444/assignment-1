Number_in_words=['Zero' ,'One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine']

while True:
 number = int(input("Enter a number from 0 to 9 : "))
 if 0 <= number <= 9:
    print('The number entered in words is : ',Number_in_words[number])
 else:
    print("Invalid Input , please enter a number between 0 and 9.")