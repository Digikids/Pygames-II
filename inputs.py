# User inputs
print("What is your name?")
name = input()
print("Hello " + name)

print("What is your age?")
age = input()
if int(age) >= 18:
    print("You are an adult")
else:
    print("You are a child")