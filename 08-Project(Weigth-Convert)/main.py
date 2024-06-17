weight = input("Weight: ")
Lbs_Kg = input ("(L)bs or (K)g: ")
lbs = 'l'
kilogram = 'k'

if Lbs_Kg.lower()  == lbs :
  print(f" You are { int(weight) * 0.45} kilos")
elif Lbs_Kg.lower() == kilogram :
  print(f"You are {int(weight) / 0.45} pounds")