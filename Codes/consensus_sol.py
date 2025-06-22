from collections import defaultdict

def parse_fasta(fasta_str):
    sequences = []
    current = ''
    for line in fasta_str.strip().splitlines():
        if line.startswith('>'):
            if current:
                sequences.append(current)
            current = ''
        else:
            current += line.strip()
    sequences.append(current)
    return sequences

def consensus_and_profile(sequences):
    length = len(sequences[0])
    profile = {
        'A': [0] * length,
        'C': [0] * length,
        'G': [0] * length,
        'T': [0] * length
    }

    # Build profile
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1

    # Build consensus
    consensus = ''
    for i in range(length):
        max_count = 0
        max_nuc = ''
        for nuc in 'ACGT':
            if profile[nuc][i] > max_count:
                max_count = profile[nuc][i]
                max_nuc = nuc
        consensus += max_nuc

    return consensus, profile

# Example usage:
fasta_input = ''

with open('Github/Rosalind/Datasets/rosalind_cons.txt', 'r') as file:
    for line in file:
        fasta_input+=line

sequences = parse_fasta(fasta_input)
consensus, profile = consensus_and_profile(sequences)

print(consensus)
for nuc in 'ACGT':
    print(f"{nuc}: {' '.join(map(str, profile[nuc]))}")

