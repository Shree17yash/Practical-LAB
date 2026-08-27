coded_msg=input("Enter the coded string: ")
secret_msg=input("Enter the secret msg: ")

if (secret_msg in coded_msg):
    print("The coded message is: ",coded_msg)
else:
    print("The Secret Message is wrong")