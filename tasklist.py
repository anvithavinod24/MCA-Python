word=input("enter word")
vowels=[]
for i in word:
    if i in "aeiouAEIOU":
        vowels.append(i)
print(vowels)
