s="ayzysiansdnajnzkjnkjcnxzca"
q=["a","s","i","y","c","m","q"]

freq = {}

for ch in s:
    freq[ch]=freq.get(ch,0)+1


for ch in q:
    print(freq.get(ch,0))

# print(freq)