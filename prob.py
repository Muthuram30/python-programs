def count_subsequence(genome="AGGCTATTGCTTTGCT", sequence="GCT"):
    print(genome.count(sequence))

genome=input("Enter the string")
sequence=input("Enter the string to check")
count_subsequence(genome,sequence)