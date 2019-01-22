# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def first_missing_positive(nums):
  s = set(nums)
  i = 1
  while i in s:
    i +=1
  return i

def first_missing_positive2(nums2):
  if not nums2:
    return 1
  for i, num in enumerate(nums2):
    while i + 1 != nums2[i] and 0 < nums2[i] <= len(nums2):
      v = nums2[i]
      nums2[i], nums2[v-1] = nums2[v-1], nums2[i]
      nums2[v-1] = v
      if nums2[i] == nums2[v-1]:
        break
  
  for i, num in enumerate(nums2, 1):
    if num != i:
      return i
  
  return len(nums2) + 1

print(first_missing_positive([3, 4, -1, 1]))

print(first_missing_positive2([3, 4, -1, 1]))