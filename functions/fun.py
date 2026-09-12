# # sum of two number
# def sum(a,b):
#   s = a + b
#   return s
# ans = sum(3 , 4)
# print("sum of two numbers=", ans)

# # even or odd number
# def check(num):
#   if(num %2 == 0):
#     return "even"
#   else:
#     return "odd"
# n = int(input("enter a number:"))
# result = check(n)
# print("The number is", result)


# # factorial of a number
# def factorial(n):
#   fact = 1
#   for i in range(1, n+1):
#     fact *= i
#   return fact
# print("factorial of a number=", factorial(5))


# # prime number 
# def prime(n):
#   if n < 2:
#     return False
#   for i in range(2, n):
#     if n % i == 0:
#       return False
#   return True
# if prime(7):
#   print("prime number")
# else:
#   print("not a prime number")


# palindrome number
def palindrome(n):
    return str(n) == str(n)[::-1]

n = input("Enter number: ")

if palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")