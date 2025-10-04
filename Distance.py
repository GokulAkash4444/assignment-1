
print("1. Miles to Kilometers")
print("2. Kilometers to Miles")

choice = input("Enter 1 or 2: ")

if choice == "1":
    miles = float(input("Enter miles: "))
    km = miles * 1.60934
    print("Kilometers:", km)
elif choice == "2":
    km = float(input("Enter kilometers: "))
    miles = km / 1.60934
    print("Miles:", miles)
else:
    print("Wrong choice")
