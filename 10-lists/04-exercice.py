#Write a program to remove the duplication in a list 

numbers = [1,3,3,5,4,4,8]
uniques = []
for number in numbers:
   if number not in uniques:
     uniques.append(number)

uniques.sort()

print(uniques)
  