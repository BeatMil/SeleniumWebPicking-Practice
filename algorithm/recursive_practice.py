# make factorial func

def factorial(n):
    text = ""
    a = 1
    if n == 1:
        return 1
    else:
        for i in range(n+1):
            if i != 0:
                a *= i
                text += "%s*" % i
        print(text[:-1])
        return a

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)

print(factorial(5))
print(factorial_recursive(5))