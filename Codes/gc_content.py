def gc_content(str):
  gc=0
  for i in str:
    if i=='G' or i=='C':
      gc+=1
  return gc/len(str)

def read_fasta(str):
   seq=''
   id=''
   for i in str:
      if i=='>':
         seq=str.split('\n')

fasta_records = {}
current_header = None

with open('01. June/Rosalind Problem/Datasets/rosalind_gc.txt', 'r') as file:
   for line in file:
      if line.startswith('>'):
        fasta_records[line[1:len(line)-1]]=''
        current_header=line[1:len(line)-1]
      else:
         fasta_records[current_header]+=(line.strip())

max_gc=0
max_ind=''

for i in fasta_records:
   curr=gc_content(fasta_records[i])
   if curr>max_gc:
      max_gc=curr
      print(curr, fasta_records[i], i)
      max_ind=i

print ('\n\n\n')
print(max_ind, max_gc*100)
