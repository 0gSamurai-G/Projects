'''
Experiment No. 1 : In a second year computer engineering class, group A students play cricket, group B students play
                   badminton and group C students play football.
                   Write a python program using functions to compute following:
                   a) List of students who play both cricket and badminton.
                   b) List of students who play either cricket or badminton but not both.
                   c) Number of students who play neither cricket nor badminton.
                   d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)
'''
#function for removing duplicate elements

def removeduplicate(a):
    re=[]
    for i in a:
        if i not in  re:
            re.append(i)
    return re

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find interscetion 

def intersection(lst1,lst2):
    inter=[]
    for i in lst1:
        if i in lst2:
            inter.append(i)
    return inter

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find union

def union(lst3,lst4):
    uni=lst3.copy()
    for i in lst4:
        if i not in uni:
            uni.append(i)
    return uni

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find difference

def diff(lst5,lst6):
    dif=[]
    for i in lst5:
        if i not in lst6:
            dif.append(i)
    return dif

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find symmetric difference

def sydiff(lst7,lst8):
    sdif=[]
    dif1=diff(lst7,lst8)
    dif2=diff(lst8,lst7)
    sdif=union(dif1,dif2)
    return sdif

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find list of students who play both cricket and badminton

def cab(lst1,lst2):
    lst3=intersection(lst1,lst2)
    print("\nList of students who play both cricket and badminton = ",lst3)
    return len(lst3)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find list of students who play either cricket or badminton but not both

def cobbnb(lst1,lst2):
    lst3=sydiff(lst1,lst2)
    print("\nList of students who play either cricket or badminton but not both = ",lst3)
    return len(lst3)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find number of students who play neither cricket nor badminton

def ncnb(lst1,lst2,lst3):
    lst4=diff(lst1,union(lst2,lst3))
    print("\nNumber of students who play neither cricket nor badminton = ",lst4)
    return len(lst4)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function to find number of students who play cricket and football but not badminton

def cafbnb(lst1,lst2,lst3):
    lst4=diff(intersection(lst1,lst2),lst3)
    print("\nNumber of students who play cricket and football but not badminton = ",lst4)
    return len(lst4)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#main function
#list of total students in se comp

secom=[]
n=int(input("\n\nEnter the no. of students in se comp = "))
for i in range(0,n):
    std=input()
    secom.append(std)
print("Original list of students = " + str(secom))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#list of cricket

cricket=[]
c=int(input("\n\nEnter the no. of students who play cricket = "))
for i in range(0,c):
    std1=input()
    cricket.append(std1)
print("\nOriginal list of students who play cricket = " +str(cricket))
cricket=removeduplicate(cricket)
print("\nList of students who play cricket after removing duplicate entries = " +str(cricket))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#list of football

football=[]
f=int(input("\n\nEnter the no. of students who play football = "))
for i in range(0,f):
    std2=input()
    football.append(std2)
print("\nOriginal list of students who play football = " +str(football))
football=removeduplicate(football)
print("\nList of students who play football after removing duplicate entries = " +str(football))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#list of badminton

badminton=[]
b=int(input("\n\nEnter the no. of students who play badminton = "))
for i in range(0,b):
    std3=input()
    badminton.append(std3)
print("\nOriginal list of students who play badminton = " +str(badminton))
badminton=removeduplicate(badminton)
print("\nList of students who play badminton after removing duplicate entries = " +str(badminton))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

a=1
while a==1:
    print("\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MENU >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("1.List of students who play both cricket and badminton.")
    print("2.List of students who play either cricket or badminton but not both.")
    print("3.Number of students who play neither cricket nor badminton.")
    print("4.Number of students who play cricket and football but not badminton.")
    print("5.Exit")

    sw=int(input("select an option = "))

    if sw==1:
        print("\nList of students who play both cricket and badminton : ", cab(cricket,badminton))
        x=input("do you want to continue (yes/no)")
        if x=="yes":
            a=1
        else:
            a=0
            print("<<< you are most welcome >>>")


    if sw==2:
        print("\nList of students who play either cricket or badminton but not both : ", cobbnb(cricket,badminton))
        x=input("do you want to continue (yes/no)")
        if x=="yes":
            a=1
        else:
            a=0
            print("<<< you are most welcome >>>")

    if sw==3:
        print("\nNumber of students who play neither cricket nor badminton : ", ncnb(football,cricket,badminton))
        x=input("do you want to continue (yes/no)")
        if x=="yes":
            a=1
        else:
            a=0
            print("<<< you are most welcome >>>")

    if sw==4:
        print("\nNumber of students who play cricket and football but not badminton : ", cafbnb(cricket,football,badminton))
        x=input("do you want to continue (yes/no)")
        if x=="yes":
            a=1
        else:
            a=0
            print("<<< you are most welcome >>>")

    if sw==5:
        print("<<< you are most welcome >>>")


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   END OF PROGRAM   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





    
        
        
    



    

