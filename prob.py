def count_subsequence(genome="AGGCTATTGCTTTGCT", sequence="GCT"):
    count = 0
    lens = 0
    leng = 0
    index = 0
    seq_list = []

    # build sequence list and its length
    for k in sequence:
        seq_list.append(k)
        lens += 1

    # length of genome
    for m in genome:
        leng += 1

    # sliding window comparison
    for i in genome:
        l = []
        if (index + lens) > leng:
            break
        for j in range(0, lens):
            l.append(genome[index + j])
        if l == seq_list:
            count += 1
        index += 1

    print("The number of occurrence is:", count)


genome = input("Enter the string: ")
sequence = input("Enter the string to check: ")
count_subsequence(genome, sequence)
