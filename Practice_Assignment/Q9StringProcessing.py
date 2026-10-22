
def stringfunctions(str):
    vowels=['a','e','i','o','u']
    countvowels=0
    countdigits=0
    countspace=0
    countconsonants=0
    for char in str:
        char=char.lower()
        if char in vowels:
              countvowels=countvowels+1
        elif char.isdigit():
            countdigits=countdigits+1
        elif char.isspace():
            countspace=countspace+1
        elif char.isalpha():
            countconsonants=countconsonants+1
    return countvowels,countconsonants,countspace,countdigits
v,c,s,d=stringfunctions("python 1 2 3")
print(" Vowels : " ,v)
print("Consonants : ",c)
print("Spaces : ",s)
print("Digits : ",d)