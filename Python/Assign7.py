def takeinput():
  fats=int(input("Enter the number of fats: "))
  carbs=int(input("Enter the number of carbs: "))
  protein=int(input("Enter the number of protein: "))
  intake={"Fats":fats,"Carbs":carbs,"Protein":protein}
  return intake
def calculate():
  overallintake=takeinput()
  calories=((overallintake["Fats"]*9.0)+(overallintake["Carbs"]*4.0)+(overallintake["Protein"]*4.0))
  return calories
def main():
  totcal=calculate()
  print("The total caloric intake is: ",totcal)

if __name__ == "__main__":
    main()
