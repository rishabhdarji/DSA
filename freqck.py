n = [5,3,2,2,1,5,5,7,5,10]
m= [10,111,1,9,5,67,2]

nums = n
an = m
freq_map={}

for i in range(0, len(nums)):

    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1

for i in range(0, len(freq_map)):
    
    if an[i] in freq_map:
        print(freq_map[nums[i]])
    else:
        print(freq_map)

# print(freq_map)

