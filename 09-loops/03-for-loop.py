# for item in ['Mosh', 'Mel', 'Manuela', 'William']:
#   print(item)

#started = 5, ended = n - 1 => 20 -1 19  
for item in range(5, 20):
  print(item)
  
  # step  if we stated from 1 to 20 and we define step 2 the output will be 1 -> 3 -> 5 ... 19
print('---------------------------------')
for i in range(1, 20, 2):
  print(i)

# exercise 

prices = [10, 20, 30]

total = 0

for price in prices:
  total += price
print(f"Total is: {total}")

