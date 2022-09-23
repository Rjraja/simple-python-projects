import random
#function for remove common letters
def commonchar(name1,name2):
  c=list(set(name1)^set(name2))
  return len(c)
#get input from user
print("welcome to Flames !")
str1=input("Enter first name :")
str2 =input("Enter second name :")
#to check is empty
if str1 == '' :
    print("Enter your first name")
elif str2 == '':
     print("Enter your second name")
# To check is numbers 
elif str1.isdigit():
    print("Enter only characters")
elif str2.isdigit():
    print("Enter only characters")
else:
    name2=str2.lower()
    name1=str1.lower()
    c=commonchar(name1.replace(' ',''),name2.replace(' ',''))
    result= ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    while len(result) > 1 :  
           splitIndex = (c % len(result) - 1)  
           if splitIndex >= 0 :  
               right = result[splitIndex + 1 : ]  
               left = result[ : splitIndex]  
               result = right + left  
           else :  
               result = result[ : len(result) - 1]  
   # print final result
    print("Relationship Status :", result[0])
    if result[0] == "Friends":
       percentage=random.randint(60,80)
    if result[0] == "Lovers":
       percentage=random.randint(80,100)
    if result[0] == "Marriage":
       percentage=random.randint(70,100)
    if result[0] == "Affection":
       percentage=random.randint(30,50)
    if result[0] == "Siblings":
       percentage=random.randint(60,90)
    if result[0] == "Enemies":
       percentage=random.randint(0,20)
    print(f" your love percentage is :{percentage} %")