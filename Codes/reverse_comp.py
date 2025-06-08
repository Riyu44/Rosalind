def compliment(str):
  new_str=""
  for i in str:
    if i=='A':
      new_str+='T'
    elif i=='T':
      new_str+='A'
    elif i=='C':
      new_str+='G'
    elif i=='G':
      new_str+='C'    
  return new_str

# with open('01. June\Rosalind Problem\Datasets\rosalind_revc.txt', 'r') as file:
#     s = file.read()
s= input()

rev_s = s[::-1]
print(rev_s)
print(compliment(rev_s))
