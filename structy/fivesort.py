def five_sort(nums):
  i = 0
  j = len(nums) - 1
  while i < j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      j -= 1
    else:
      i += 1

  return nums
  pass # todo

print(five_sort([12, 5, 1, 5, 8, 5]))