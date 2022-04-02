# In a exam students have access of this python program
# but calculator is restricted to use in exam
# Any student try to use this calculator ans will be wrong
# for these calculations only, since this was given in exam
# faulty as: 45*3 = 555, 56+9=77, 56/6=4;
# if cheater student try to solve small example it will show right ans.
# like 1+1=2, 2*5=10
while(1):
    op = input("Enter your choice of Operator, * + / - :\nOr,want to stop calculator? enter y :")    
    if(op=="y"):
        break
    else:
        print("Enter two numbers:")
    a = int(input("enter 1st no. :"))
    b = int(input("enter 2nd no. :"))

    if (op=="*"):
        if(a==45 and b==3):
           print(555)
        else:
            print(a*b)
                 
    elif (op=="+"):
        if(a==56 and b==9):
            print(77)
        else:
            print(a+b)
        
    elif (op == "/"):
        if(a==56 and b==6):
            print(4)
        else:
            print(a/b)
        
    elif(op=="y"):
        break
    else:
        print("Enter a valid choice")
              
