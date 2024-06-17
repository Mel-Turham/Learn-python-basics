# If temperature is greater than 30 
  # it's a hot day
#otherwise if it's less than 10
  # it's a cold day
# otherwise
  # it's neither hot or cold
  
  # <, > <= , >= , ==, !=
temperature = 30

if temperature > 30 :
  print(" it's a hot day")
elif temperature < 10:
  print("It's a cold day")
else:
  print("it's neither hot or cold day")
  
  
# exercise 
 # if name is less than 3 characters long 
  #name must be at least 3 characters 
#otherwise if it's more than 50 characters long 
 #name can be a maximum of 50 characters
#otherwise 
  #name looks good

name = input("What's your name? ")

if len(name) < 3 :
  print("name must be at least 3 characters ")
elif len(name) > 50 :
  print("name can be a maximum of 50 characters")
else:
  print("name looks good!!")