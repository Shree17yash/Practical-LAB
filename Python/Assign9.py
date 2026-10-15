while (True):
  op=int(input("Enter the operation to be performed:\n1)Read the File\n2)Rewrite in the File\n3)Append a File\n4)Exit\nEnter the choice: "))

  if(op==1):
    path=input("Enter the path of the File:")
    with open(path,"r") as file:
      content=file.read()
      print(content)
  elif(op==2):
    path=input("Enter the path of the File:")
    strg=input("Enter the string to rewrite")
    with open(path,"w") as file:
      file.write(strg)
  elif(op==3):
    path=input("Enter the path of the File:")
    strg=input("Enter the string to add")
    with open(path,"a") as file:
      file.write("\n"+strg)
  elif(op==4):
    print("Exiting the program....")
    break
  else:
    print("Invalid choice")
