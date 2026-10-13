n = int(input("Enter a number: "))
number = n
num = n

cnt = 0
if n==0:
    cnt = 1
else:
    while n>0:
        cnt += 1
        n //= 10

# print(cnt)

# If you want to compute the time complexity of anything which is divided by 10 then it is O(Log10(n)),
#  similarly if divided by 2 then it is O(Log2(n)).


# Reverse the number 
sum = 0
reverseNum = 0
while number > 0:
    lastDig = number % 10
    sum = sum + (lastDig * lastDig * lastDig)
    reverseNum = (reverseNum * 10) + lastDig
    number //= 10

# print(reverseNum)

# pallendrome 
# save a duplicate of the number and then check it if the number is same as 
# the reverse of the number

if num == reverseNum:
    print("Pallendrome")
else:
    print("Not Pallendrome")

# ArmStrong number is something 
# For example: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
# 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
# 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")


# printing all the division

for i in range(1, n):
    if ( n%i == 0):
        print(i)
        
    else:
        print("Not a perfect number")

