# Reverse the array using Recursion
def func(num,left,right):
    if left>=right:
        return
    num[left],num[right] = num[right], num[left]

    func(num, left+1,right-1)
    
num=[5,7,3,2,6,1,5,9]
func(num, 3, 5)
print (num)

time complexity is N/2 as we did half operations O(N/2)
Space complexity is also N/2 same half operations so n/2.
