def probab(k, m, n):
  total = k+m+n
  return 1-  (m*m +4*n*n +4*m*n -4*n - m)/(4*total*total - 4*total)

test = []
with open('Roaslind/Datasets/rosalind_iprb.txt', 'r') as file:
  for line in file:
    test.append(line.split(' '))

# print(test[0])
print(probab(int(test[0][0]), int(test[0][1]), int(test[0][2])))