def sayHello(name):
    print('Hello ' + name)

sayHello("Alice")
sayHello("Tomorrow")

def add(a, b, c, d):
    print(a + b + c + d)

add(10, 20, 30, 40)

def returnEven(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    print(even)

returnEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])