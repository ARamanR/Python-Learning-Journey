# 4. Write a program to sum a list with 4 numbers.

a=[1,2,3,4]
print(sum(a))

# Try with Input from user
numbers = []
for i in range(4):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)
print("The list of numbers is:", numbers)
print("The sum of the numbers is:", sum(numbers))


