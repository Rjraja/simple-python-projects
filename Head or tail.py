import random
for i in range(10):
    start=input("click to start!")
    list=[0,1,2,3,4,5,6,7,8,9,10]
    value=random.choice(list)
    if((value%2)==0):
        print("tail")
    else:
        print("head")
