#stack implementing using list
#Last In First Out

stack=[]

def push():
    if len(stack)==n:
        print("Stack Is Over")
    else:
        element=int(input("Enter number"))
        stack.append(element)
        #print(stack)
def pop():
    if not stack:
        print("No element at the stack")
    else:
        e=stack.pop()
        print("Removed element",e)
        print(stack)
def display():
    print(stack)

n=int(input("How Many Times You Enter A Number In To The Stack"))
while True:
    print("Enter choise 1 for enter element","\n",
          "2 for remove elment","\n","3 for Display","\n","4 for exit")
    ch=int(input())
    print(ch)

    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        quit()
    else:
        print("Invalid choise")