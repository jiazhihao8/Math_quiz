import random
menu='''
************************
** A Simple Math Quiz **
************************
1. Addition
2. Subtraction
3. Multiplication       
4. Integer Division     
5. Exit
------------------------
'''
correcttimes=0
ask_times=0
def Addition(ask_times,correcttimes):
    for i in range(0,3):
        a=random.randrange(0,50)
        b=random.randrange(0,50)
        print(a,"+",b)
        answer=int(input())
        if answer==a+b:
            print("Correct")
            correcttimes+=1
            ask_times+=1
        else:
            ask_times+=1
    accuracy_rate=100*correcttimes/ask_times
    print("accuracy_rate is",accuracy_rate,"%")  
def Subtraction(ask_times,correcttimes):
    for i in range(0,3):
        a=random.randrange(20,50)
        b=random.randrange(1,20)
        print(a,"-",b)
        answer=int(input())
        if answer==a-b:
            print("Correct")
            correcttimes+=1
            ask_times+=1
        else:
            ask_times+=1
    accuracy_rate=100*correcttimes/ask_times
    print("accuracy_rate is",accuracy_rate,"%")
def Multiplication(ask_times,correcttimes):
    for i in range(0,3):
        a=random.randrange(0,20)
        b=random.randrange(0,10)
        print(a,"*",b)
        answer=int(input())
        if answer==a*b:
            print("Correct")
            correcttimes+=1
            ask_times+=1
        else:
            ask_times+=1
    accuracy_rate=100*correcttimes/ask_times
    print("accuracy_rate is",accuracy_rate,"%")    
def Integer_Division(ask_times,correcttimes):
    for i in range(0,3):
        a=random.randrange(10,50)
        b=random.randrange(1,10)
        print(a,"//",b)
        answer=int(input())
        if answer==a//b:
            print("Correct")
            correcttimes+=1
            ask_times+=1
        else:
            ask_times+=1
    accuracy_rate=100*correcttimes/ask_times
    print("accuracy_rate is",accuracy_rate,"%")
game=int(input(menu))
if game==1:
    Addition(ask_times,correcttimes)
elif game==2:
    Subtraction(ask_times,correcttimes)
elif game==3:
    Multiplication(ask_times,correcttimes)
elif game==4:
    Integer_Division(ask_times,correcttimes)
elif game==5:
    print("bye")