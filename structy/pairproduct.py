def pair_product(numbers, target_product):
#   divisors = {}
#   for index, num in enumerate(numbers):
#     if num != 0 and target_product % num == 0:
#       divisor = target_product // num
#       if divisor in divisors:
#         return (divisors[divisor], index)

#       divisors[num] = index
  pass # todo

  # Step 1: Create a dictionary to track divisors
  divisors = {}
  
  # Step 2: Iterate through the list
  for index, num in enumerate(numbers):
      # Step 3: Avoid division by zero
      if num != 0 and target_product % num == 0:
          # Check if the current number is a divisor
          divisor = target_product // num
          if num in divisors:
              return (divisors[num], index)
          
          # Step 4: Store the divisor in the dictionary
          divisors[divisor] = index

print(pair_product([3, 2, 5, 4, 3], 8))