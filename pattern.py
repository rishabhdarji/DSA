# n=int(input("Enter the number of rows: "))


def print3(n:int) ->None:
    for i in range(n):
        for j in range(1, i+2 ):
            print(j, end=" " )
        print()
    pass

def print4(n:int) ->None:
    for i in range(1,n):
        for j in range(1, i+1):
            print(i, end=" " )
        print()

def print5(n:int) ->None:
    for i in range(n):
        for j in range(1, n-i+1):
            print("*", end=" " )
        print()

def print6(n:int) ->None:
    for i in range(n):
        for j in range(1, n-i+1):
            print(j, end=" " )
        print()

def print7(n:int) ->None:
    for i in range(n):
        for j in range(i):
            print(" ", end="" )
        for j in range(n-i-1):
            print("*", end="" )
        for j in range(n-i):
            print("*", end="")
        print()
# Alternate solution for print7
def print8(n:int) ->None:
    for i in range(n):
        for j in range(i):
            print(" ", end="" )
        for j in range(2*(n-i)-1):
            print("*", end="" )
        print()
# more alternate of it 
def print9(n:int) ->None:
    for i in range(n):
        for j in range(i):
            print(" ", end="" )
        for j in range(2*n -2*i-1):
            print("*", end="" )
        for j in range(i):
            print(" ", end="")
        print()
def print10(n:int) ->None:
    for i in range(n):
        for j in range(i):
            print(" ", end="" )
        for j in range(2*n -2*i-1):
            print("*", end="" )
        print()

def print11(n:int) ->None:
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="" )
        for j in range(2*i+1):
            print("*", end="" )
        for j in range(n-i-1):
            print(" ", end="")
        print()

# full pyramid code
def print12(n:int) ->None:
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="" )
        for j in range(2*i+1):
            print("*", end="" )
        for j in range(n-i-1):
            print(" ", end="")
        print()
    for i in range(n):
        for j in range(i):
            print(" ", end="" )
        for j in range(2*n -2*i-1):
            print("*", end="" )
        print()
    
def print13(n:int) ->None:
    for i in range(1, 2*n-1):
        stars = i
        if i>n:
            stars = 2*n-i
        for j in range(1, stars):
            print("*", end=" " )
        print()

n=5# right angle triangle 01
def print14(n:int) ->None:
    start = 1
    for i in range(1, n):
        if(i%2==0):start = 1
        else: start = 0
        for j in range(1, i):
            print(start, end="" )
            start = 1-start
        print()

# V shape n numbers printing pattern 
def print15(n:int) ->None:
    space = 2 * (n-1)
    for i in range (0, n):
        # numbers
        for j in range(1, i+1):
            print(j, end=" ")    
        #space
        for k in range(space):
            print(" ", end=" ")
        #numbers
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()
        space -= 2
        
def print16(n:int) ->None:
    counter = 1
    for i in range(0,n):
        for j in range(0, i+1):
            print(counter, end=" ")
            counter += 1
        print()
        
def print17(n:int) ->None:
    counter = 'A'
    for i in range(0,n):
        for j in range(0, i+1):
            print(counter, end=" ")
            counter = chr(ord(counter) + 1)
        print()

# A
# AB
# ABC
# ABCD
def print18(n:int) ->None:
    for i in range(0,n):
        counter = chr(ord('A'))
        for j in range(0, i+1):
            print(counter, end=" ")
            counter = chr(ord(counter) + 1)
        print()

# ABCD
# ABC
# AB
def print19(n:int) ->None:
    for i in range(0,n):
        counter = chr(ord('A'))
        for j in range(n, i, -1):
            print(counter, end=" ")
            counter = chr(ord(counter) + 1)
        print()

def print20(n:int) ->None:
    counter = chr(ord('A'))
    for i in range(0,n):
        counter = chr(ord('A')+ i)
        for j in range(0, i + 1):
            print(counter, end=" ")
        print()

def print21(n:int) ->None:
   
    for i in range(n):
        counter = chr(ord('A'))
       
        for j in range(n-i-1):
            print(" ", end=" ")
        
        for j in range(0, 2*i + 1):
            print(counter, end=" ")
            
            if j < i:
                counter = chr(ord(counter) + 1)
            else:
                counter = chr(ord(counter) - 1)
        print()
        
# E 
# D E 
# C D E
# B C D E
# A B C D E
def print22(n:int) ->None:
    counter = chr(ord('A'))
    for i in range(0, n):
        counter = chr(ord('A') + n - i -1)
        for j in range(0, i + 1):
            print(counter, end=" ")
            counter = chr(ord(counter) + 1)
        print()

# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
def print23(n:int) ->None:
    # stars
    for i in range(0,n):
        for j in range(n, i, -1):
            print("*", end=" ")
    # space 
        for j in range(0, 2*i):
            print(" ", end=" ")
    # stars
        for j in range(n,i,-1):
            print("*", end=" ")
        print()
    
    for i in range(0,n):
        for j in range(0, i+1):
            print("*", end=" ")
        for j in range(0, 2*(n-i-1)):
            print(" ", end=" ")
        for j in range(0, i+1):
            print("*", end=" ")
        print()

# *                 * 
# * *             * * 
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
def print24(n:int) ->None:
    space = 2*n -2
    for i in range(0, 2*n-1):
        star = i

        if i>=n:
            star = 2*n-i -2 
        # star 
        for j in range(0, star + 1):
            print("*", end=" ")

        # Space     
        for j in range(0, space):
            print(" ", end=" ")

        # Star 
        for j in range(0, star + 1):
            print("*", end=" ")  

        print()
        if i < n -1 :
            space -= 2
        else:
            space += 2

# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *       
def print25(n:int) ->None:
    for i in range(0,n):
        for j in range(0, n):
            if i==0 or j ==0 or i == n-1 or j== n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print26(n:int) ->None:
    for i in range(0,2*n-1):
        for j in range(0, 2*n-1):
            top = i
            left = (2*n-2) - j 
            bottom = (2*n-2) - i
            right =j
            print(n- min(min(top,bottom), min(left, right)), end=" ") 
        print()
print26(int(n))