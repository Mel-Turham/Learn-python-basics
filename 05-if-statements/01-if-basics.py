is_hot = False
is_cold = False

if is_hot:
  print("it's hot day")
  print('Drink plenty of water')
elif is_cold:
   print('Is a cold day')
   print('Wear a warm clothes')
else:
  print("it's a lovely day")

print('Enjoy your day')

# Exercise Price of house is $1M if buyer has good credit , they need to put down 10%, Otherwise they need to put down 20% and print the down payment

house_price = 1000000

has_good_credit = True

if has_good_credit:
  down_payment = 0.1 * house_price
else:
  down_payment = 0.2 * house_price
  
print(f'Down payment: ${down_payment}')