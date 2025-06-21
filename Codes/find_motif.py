# function to find substring in a string
def substring(s, t):
    index = ''
    for i in range(0, len(s)):
        if s[i:i+len(t)]==t:
            #print(s[i:i+len(t)])
            index += str(i+1) + ' '
    return index

with open('Github/Rosalind/Datasets/rosalind_subs.txt', 'r') as file:
    inputs = []
    for line in file:
        inputs.append(line.strip())

print(inputs[1])

print(substring(inputs[0], inputs[1]))
