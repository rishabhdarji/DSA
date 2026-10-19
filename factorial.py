def func(N):
    if N==0 or N==1:
        return 1 
    return N * func(N-1)

x = int(input("Enter a number:"))
print(func(x))