def hamming(str1, str2):
  distance=0
  ind=0
  for i in str1:
    if i != str2[ind]:
      distance+=1
    ind+=1
  return distance

str1=''
str2=''
with open('01. June/Rosalind Problem/Datasets/rosalind_hamm.txt', 'r') as file:
  i=0
  for line in file:
    if i==0:
      str1=line
      i+=1
    else:
      str2=line

print(hamming(str1,str2))
    