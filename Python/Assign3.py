#This Python code creates a list to store number of assignments
assign=[]
assigncomp=[]
def addassign(nameassign):
    assign.append(nameassign)
    return assign
def removeassign(nameassign):
    if nameassign in assign:
        assigncomp.append(nameassign)
        assign.remove(nameassign)
        return assign
    else:
        return "Assignment does not exist"


while(True):
    print("Enter the operation to be performed \n1)Add an assignment \n2)Remove an assignment \n3)Exit")
    check=int(input())
    
    match check:
        case 1:
            nameassign=input("Enter the assignment name: ")
            print(addassign(nameassign))
        case 2:
            nameassign=input("Enter the assignment name: ")
            print(removeassign(nameassign))
        case 3:
            break
        case _:
            print("Invalid Input")
