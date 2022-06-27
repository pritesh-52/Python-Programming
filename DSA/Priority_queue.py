#Priority queue
#remove the elements priority wised


queue=[]
def push():
    if len(queue)==n:
        print("Queue is over")
    else:
        ele=int(input("Enter Number"))
        queue.append(ele)
        #print(queue)

def pop():
        if not queue:
            print("Elements not availble in the queue")
        else:
            a=min(queue)
            queue.remove(a)   #Using this function can delete the element
            print("Removed element",a)


def display():
    if queue:
        print(queue)

n=int(input("How many times you enter elements"))
while True:
    print("Enter Number 1 for insert","\n","2 for delete","\n","3 for display","\n","4 for exit")
    ch=int(input())

    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    else:
        quit()

#Algoritm
'''
setp1:start
setp2:take the value from user how many times will enter elements in queue 
setp3:value get the from user choise bases for opertaion perform
        1)push
        2)pop
        3)display
step4: intizale the queue[] empty list
step5:take the elements from the user enter in the queue 
setp6:check condtion if user choise 1 for push
        if len(queue)==value how many times enter element in queue
            print("queue is over)
        else
            add the elements to the queue using append() method
        
step7:check condtion if user choise 2 for pop
        if not queue
            print("Elements not available")
        else
            delete the element 
            a=min(queue)
            queue.remove(a)

step 8:check condtion if user choise 3 for display
        if queue  check queue availble
            print(queue)
step 9: exit

'''