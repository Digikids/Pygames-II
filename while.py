count = 0

while count < 5:
    print("The count is", count)
    count = count + 1

while True:
    answer = input("Do you want to continue? (y/n): ")
    if answer.lower() == "n":
        break
    print("Continuing...")

i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)