#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
import math
os.system('cls')


while True:
  try:
    print("Enter in the coefficients for a quadratic equation in the format:")
    print("  ax^2 + bx + c = 0")
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    a = int(a)
    b = int(b)
    c = int(c)

    try:
      
      x = (b**2)-(4*a*c)
      x = math.sqrt(x)
      root1 = ((b*-1) + x)/(2*a)
      root2 = ((b*-1) - x)/(2*a)
      root1 = round(root1, 2)
      root2 = round(root2, 2)
      print("The roots are", root1,"and", root2)
      
    except:
      print("There are no real roots to the equation")

  except:
    print("Those are not valid values for a,b and c")

