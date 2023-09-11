# 1.1 Implement a recursive function to calculate the factorial of a given number

"""
1! = 1 × 1
2! = 2 × 1!

"""


def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)
                           
number = 3
res = fact_rec(number)

print("The factorial of {} is {}".format(number,res))