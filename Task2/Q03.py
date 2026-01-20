#Write a program that asks the user for the length and width of a rectangle. 
#The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = (length + width) * 2
area = length * width

print("The perimeter of the rectangle is", perimeter)
print("The area of the rectangle is", area)