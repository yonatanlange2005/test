


def factorial(n):
    new_num=1
    for i in range(n,1,-1):
        new_num*=i
    return new_num

print(factorial(3))