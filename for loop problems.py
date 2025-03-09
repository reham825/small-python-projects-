# Exercise 1: Display numbers from -10 to -1 using for loop
for i in range (-10, 0):
    print(i)

# Exercise 2:Print all prime numbers within a range
# A Prime Number is a number that cannot be made by multiplying other whole numbers.
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
for i in range(25, 51):
    for num in range(2, i):
        if i % num == 0:
            break
    else:
        print(i)

# Exercise 3: Find the factorial of a given number
number = 5
factorial = 1
for i in range(2, number + 1):
    factorial *= i
print(factorial)
