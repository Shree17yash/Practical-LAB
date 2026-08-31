#This program checks the password
def inputpass():
    password=input("Enter the password: ")
    return password
def passcheck(password):
    if (len(password)>8):
        up=any(char.isupper() for char in password)
        low=any(char.islower() for char in password)
        dig=any(char.isdigit() for char in password)
        return (up and low and dig)
    else:
        return False

def main():
    while True:
        chk=inputpass()
        match chk:
            case "Stop" | "Stop":
                print("Exiting...")
                break
            case _:
                if (passcheck(chk)==True):
                    print("Password is accepted")
                else:
                    print("Password is rejected please enter again")
main()