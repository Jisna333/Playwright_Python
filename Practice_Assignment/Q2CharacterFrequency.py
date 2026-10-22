word="programming"
freq={}
count=0
for char in word :
    if char in freq :
        freq[char]=freq[char]+1
    else:
        freq[char]=1
print("The dictionary representing the frequency of characters is ")
print(freq)
