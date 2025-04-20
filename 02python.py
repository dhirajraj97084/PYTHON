name1="dhiraj"
name2='neeraj'
name3="kumar"
#print first string
print(name1)
#print second string
print(name2)
# sum both string
sum=name1+name2+name3
print(sum)
#type of string
print(type(name1),type(name2),type(sum))
# length of string
print(len(name1),len(name2),len(sum))
#string array
print(name1[0])
print(name2[0])
# print(name2[7]) # error
print("my string array is :")
for x in name1:
    print(x)

#in special sequense present or not checking 
if "kumar" in sum:
    print("yes","kumar is present in sum")