codon_table = {
'UUU': 'F',      'CUU' : 'L',      'AUU': 'I',      'GUU': 'V',
'UUC': 'F',      'CUC' : 'L',      'AUC': 'I',      'GUC': 'V',
'UUA': 'L',      'CUA' : 'L',      'AUA': 'I',      'GUA': 'V',
'UUG': 'L',      'CUG' : 'L',      'AUG': 'M',      'GUG': 'V',
'UCU': 'S',      'CCU' : 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': 'S',      'CCC' : 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': 'S',      'CCA' : 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': 'S',      'CCG' : 'P',      'ACG': 'T',      'GCG': 'A',
'UAU': 'Y',      'CAU' : 'H',      'AAU': 'N',      'GAU': 'D',
'UAC': 'Y',      'CAC' : 'H',      'AAC': 'N',      'GAC': 'D',
'UAA': 'Stop',   'CAA' : 'Q',      'AAA': 'K',      'GAA': 'E',
'UAG': 'Stop',   'CAG' : 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': 'C',      'CGU' : 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': 'C',      'CGC' : 'R',      'AGC': 'S',      'GGC': 'G',
'UGA': 'Stop',   'CGA' : 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': 'W',      'CGG' : 'R',      'AGG': 'R',      'GGG': 'G'
}

def translate(str):
  i=0
  protein = ''
  while(i<len(str)):
    codon = str[i:i+3]
    if codon_table[codon] == 'Stop':
      break
    protein+= codon_table[codon]
    i+=3
  return protein


with open('Roaslind/Datasets/rosalind_prot.txt', 'r') as file:
  s = file.read()

print(translate(s))