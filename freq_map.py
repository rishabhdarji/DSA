freq_map={}
nums=[5,6,7,1,2,4,1,5,7,2,1,1,2]
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1 

   