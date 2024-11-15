
value = input("Enter value: ")

if not (value.isnumeric()):
    print("is not a number")
else:
    print("luck")

print("*"*50)

if not (value.isnumeric()):
    print("is not a number")
else:
    print("there are",len(value),"items")
    print("luck")

print("*"*50)

value1 = input("Enter value1: ")
value2 = input("Enter value2: ")

max = max(value1,value2)

if value1 == value2:
    print("are the same")
else:
    print("Max number is ",max)

print("*"*50)    

value1 = int(input("Enter value1: "))
value2 = int(input("Enter value2: "))

result = 0
for i in range(value1,value2+1):
    result += i
print("Result",result)

print("*"*50)    

value1 = input("List of numbers: ")

result = [ int(x) for x in value1.split(",") if int(x) > 0]

print(result)

print("*"*50)    

value1 = int(input("Enter value1: "))
value2 = int(input("Enter value2: "))
value3 = int(input("Enter value3: "))

result = 0
for i in range(value1,value2+1,value3):
    result += i
    print(i,"Result",result)

print("*"*50)    

c = 0
for i in range(0,50):
    c += 1    
    print("{:3}".format(i),end="")
    if c == 10:
        c = 0
        print("\n")
    