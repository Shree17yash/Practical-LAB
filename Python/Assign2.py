mass=float(input("Enter the mass of the object in kilograms: "))
def grav_earth(mass):
    weight=mass*9.806
    return weight
def grav_moon(mass):
    weight=mass*1.62
    return weight
def main():
    while(True):
        print(" \nSelect the operation")
        print("1)Calculate the weight on Earth \n2)Calculate the Weight on Moon \n3)Exit \n")
        check=int(input("Enter choice: \t"))
        match check:
            case 1:
                print("The Weight on Earth is:",grav_earth(mass))
            case 2:
                print("The Weight on Moon is:",grav_moon(mass))
            case 3:
                break
main()
