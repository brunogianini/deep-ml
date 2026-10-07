def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
  if len(a) != len(b):
    return -1

  result = []
  for x in range(len(a)):
    temp_result = []
    for y in range(len(a[x])):
      temp_result.append(a[x][y] * b[y])

    result.append(sum(temp_result))


  
  return result