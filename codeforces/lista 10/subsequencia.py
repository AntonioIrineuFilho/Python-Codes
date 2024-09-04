nseq1, nseq2 = map(int, input().split())
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))
l_indice = [[], []]

for i in range(len(seq2)):
    for j in range(len(seq1)):
        if (seq2[i] == seq1[j] and j not in l_indice[1]):
            if not (l_indice[0].count(seq1[j]) == seq2.count(seq1[j])):
                l_indice[0].append(seq1[j])
                l_indice[1].append(j)
                break
        if (seq2[i] not in seq1):
            print('N')
            quit()

if (sorted(l_indice[1]) == l_indice[1]):
    print('S')
else:
    print('N')
        
