x = 10
y = 14
z = 12

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if (x >= y) and (x >= z):
   largest = x
elif (y >= x) and (y >= z):
   largest = y
else:
   largest = z

print("The largest number is", largest)