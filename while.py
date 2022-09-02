#program to add n natural numbers

n = int(input("Enter n: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1
print("The sum is", sum)