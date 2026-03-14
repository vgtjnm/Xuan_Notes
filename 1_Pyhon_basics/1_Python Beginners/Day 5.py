#first step function

def recursion(x):
    total = x;
    for i in range(1,x):
        total += i
    return total

answer = recursion(5)
print(answer)

def student(name):
    print("Hello "+name+"!")

student("Tom")

def RS(x,total):
    if x < 1:
        return total
    else:
        return RS(x-1,total+x)

answer = RS(5,0)
print(answer)