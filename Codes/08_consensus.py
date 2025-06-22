#function to compute the consensus matrix and profile matrix
def find_consensus(l):
    map = {'A':[0]*len(l[list(l.keys())[0]]), 'C':[0]*len(l[list(l.keys())[0]]), 'G':[0]*len(l[list(l.keys())[0]]), 'T':[0]*len(l[list(l.keys())[0]])}
    for key in l:
        for i in range(len(l[key])):
            map[l[key][i]][i]+=1
    final_str=''
    for i in range(len(l[list(l.keys())[0]])):
        curr_max=0
        curr_key=''
        for key in map:
            if curr_max<map[key][i]:
                curr_max=map[key][i]
                curr_key=key
        final_str+=curr_key
                
    print(final_str)
    profile_matrix= ''
    for key in map:
        temp_str = ''
        for i in range(len(map[key])):
            temp_str += str(map[key][i]) + ' ' 
        profile_matrix += key + ': ' + temp_str
        print(key, ':', temp_str)
    return final_str + '/n' + profile_matrix

l={}

# reading the input
with open('Github/Rosalind/Datasets/rosalind_cons.txt', 'r') as file:
    curr_header=''
    for line in file:
        if line.startswith('>'):
            curr_header=line.strip()
            l[line.strip()] = ''
            continue
        else:
            l[curr_header]+=line.strip()

find_consensus(l)

