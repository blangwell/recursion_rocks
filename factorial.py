# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n, result=1):
    if n != 0:
        result *= n
        n -= 1
        return factorial(n, result)
    return result

print(factorial(4))
# => 120