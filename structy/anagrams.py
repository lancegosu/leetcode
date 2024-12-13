def anagrams(s1, s2):
  if len(s1) != len(s2):
    return False

  word1 = {}

  for i in s1:
    word1[i] = word1.get(i, 0) + 1

  for j in s2:
    if j in word1 and word1[j] > 0:
      word1[j] -= 1
    else:
      return False

  return True


print(anagrams('paper', 'reapa'))