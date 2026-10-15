
def operation():
    shape=input("Enter the shape: ")
    if(shape=="circle" or shape=="Circle" or shape=="CIRCLE"):
      radius=float(input("Enter the radius: "))
      area=3.14*radius**2
      return {"area":area,"Shape":shape}
    elif(shape=="Triangle" or shape=="triangle" or shape=="TRIANGLE"):
      base=float(input("Enter the base: "))
      height=float(input("Enter the height: "))
      area=(1/2)*base*height
      return {"area":area,"Shape":shape}
    elif(shape=="Rectangle" or shape=="rectangle" or shape=="RECTANGLE"):
      s1=float(input("Enter the side 1: "))
      s2=float(input("Enter the side 2: "))
      area=s1*s2
      return {"area":area,"Shape":shape}
    else:
      print("Invalid shape")
      return None
def main():
  val=operation()
  print("The shape is ",val["Shape"]," and the area is ",val["area"])
if __name__ == "__main__":
    main()
