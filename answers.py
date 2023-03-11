# Write a function that takes two parameters, a and b,
# and returns their sum.
def add_numbers(a, b):
    sum = a + b
    print(sum)

add_numbers(5, 7)

# Write a function that takes a list of integers and returns
# the sum of all the even numbers in the list.
def sum_even_number(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    print(total)

sum_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Write a for loop that prints the numbers from 1 to 10.
for num in range(1,11):
    print(num)

# Write a for loop that iterates over a list of strings and
# prints each string in lower.
words = ["HELLO", "WORLD", "PYTHON"]
for word in words:
    print(word.lower())

# Write a while loop that prints the numbers from 1 to 10.
num = 1
while num <= 10:
    print(num)
    num = num + 1

# Write a while loop that takes user input until the user
# enters the word "quit".
user_input = ""
while user_input != "quit":
    user_input = input("Enter a word (or 'quit' to exit): ")
    print("You entered:", user_input)
