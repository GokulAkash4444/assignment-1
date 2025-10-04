import math

print("Finding the roots of quadratic equation ax^2 + bx + c = 0")

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b*b - 4*a*c  

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and different")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d == 0:
    root = -b / (2*a)
    print("Roots are real and same")
    print("Root =", root)
else:
    realPart = -b / (2*a)
    imagPart = math.sqrt(-d) / (2*a)
    print("Roots are complex")
    print("Root 1 =", realPart, "+", imagPart, "i")
    print("Root 2 =", realPart, "-", imagPart, "i")
