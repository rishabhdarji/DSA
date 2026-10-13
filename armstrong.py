# n=int(input("Enter a number: "))
# node =len(str(n))
# num =n 
# total = 0
# while num>0:
#     Ld = num % 10
#     total = total + (Ld ** node)
#     num = num // 10

# if total == n:
#     print("It is an Armstrong number")
# else:
#     print("It is not an Armstrong number")
from math import sqrt

# Numbers are divisible or not (THIS SOLUTION IS THE BRUTE FORCE SOLUTION)
n = int(input("enter a number"))
list = []
# for i in range(1, n+1):
#     if n%i==0:
#         list.append(i)
# print(list)
# The time complexity of this solution is O(n), and space complexity is O(k), where k i the amount of factors 

# THE BETTER SOLTUION OF THIS PROBLEM

# for i in range (1, n//2):
#     if n%i == 0:
#         list.append(i)
# list.append(n)
# print(list)
# the time complexity of this solution is O(n/2) and space complexity is O(k), where k is the amount of factors.


# Now this is the Optimal solution
for i in range(1, int(sqrt(n)+1)):
    if n%i == 0:
       list.append(i)
       if n//i != i:
        list.append(n//i)
# list.append(n) 
list.sort()
print(list)