n = [5,3,2,2,1,5,5,7,5,10]
m= [10,111,1,9,5,67,2]

# Condition is n[i] is between 1 to 10, and n and m can be 10**8

# dictlist=[0]*11
# for num in n:
#     dictlist[num]+=1
# for num in m:
#     if 1 <= num >= 10:
#         print(0)
#     else:
#         print(dictlist[num])

# Same with freq mapping.
num = n
freq_map={}
for i in range (0, len(n)):

    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1

print(freq_map)