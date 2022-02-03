# Function to print the submasks of N
def SubMasks(N) :
    S = N
    while S > 0:
        print(S)
        S = (S - 1) & N
