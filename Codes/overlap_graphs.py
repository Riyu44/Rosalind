fasta_records = {}
current_header = None

with open('Github/Rosalind/Datasets/rosalind_dna.txt', 'r') as file:
   for line in file:
      if line.startswith('>'):
        fasta_records[line[1:len(line)-1]]=''
        current_header=line[1:len(line)-1]
      else:
         fasta_records[current_header]+=(line.strip())

print(fasta_records)