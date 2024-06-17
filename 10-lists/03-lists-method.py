numbers = [3,4,5,6,7,8,5,5]
# added numbers at the end 
numbers.append(9)

# insert(index, value)
numbers.insert(0, 30)
# remove one item in ours lists remove(item)
numbers.remove(3)
# pop() remove the last item in the list
numbers.pop()
#index()
print(numbers.index(5))
# count()
print(numbers.count(5))

# sort
numbers.sort()
#reverse
numbers.reverse()
# copy()
second_numbers = numbers.copy()
numbers.clear()
print(second_numbers)
print(numbers)

# remove all item in ours list is clear() method
# numbers.clear()

# in method to check if we have an existing item in ours list
print( 8 in numbers)
print(numbers)