n = [5,3,2,2,1,5,5,7,5,10]
m= [10,111,1,9,5,67,2]
freq_map = {}

for i in range(0, len(n)):
    freq_map[n[i]]=freq_map.get(n[i],0)+1

for x in m:
    print("The number",x,"appears", freq_map.get(x,0),"times")