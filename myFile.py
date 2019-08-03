x=15
y=3
z = "This"

#Concatenate strings
print(z*y)

#Automated spacing
print(x,y,z)

#For loop
for i in range(0,10):
    print(i)

#List
myList = [10,20,30,40]

for i in myList:
    print(i.index())

#Function
def myPrint(words):
    print(words, ", ok.")

myPrint("are you")

def recFun(vList):
    if len(vList) > 0:
        print(vList.pop())
        recFun(vList)

recFun([1,"star",3.14, "Hi Hi"])

#While
while x > 0:
    print(x)
    x = x - 1

def myRecFun(vList,index,step):
    if index < len(vList):
        print(vList[index])
        myRecFun(vList,index + step,step)
    
myRecFun([1,2,3,4],0,2)