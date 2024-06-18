def find_max(numbers):
  max_number = numbers[-1]
  for number in numbers:
    if (number > max_number):
      max_number = number
  return max_number