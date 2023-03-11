# Write a function that takes two parameters, a and b,
# and returns their sum.
def add_numbers(a, b):
    print(a + b)

# Write a function that takes a list of integers and returns
# the sum of all the even numbers in the list.


def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    print(total)


# Write a for loop that prints the numbers from 1 to 10.
for num in range(1, 11):
    print(num)

# Write a for loop that iterates over a list of strings and
# prints each string in lower.
words = ["hello", "world", "python"]
for word in words:
    print(word.upper())

# Write a while loop that prints the numbers from 1 to 10.
num = 1
while num <= 10:
    print(num)
    num += 1

# Write a while loop that takes user input until the user
# enters the word "quit".
user_input = ""
while user_input != "quit":
    user_input = input("Enter a word (or 'quit' to exit): ")
    print("You entered:", user_input)
