# The pyramidal number P_N represents the number of blocks needed to build a square pyramid with an N \times NN×N base. It can be calculated using the fact that a single N \times NN×N contains N^2 blocks.
# P_1 = 1^2
# P_2 = 1^2 + 2^2
# P_3 = 1^2 + 2^2 + 3^2
# P_N = 1^2 + 2^2 + ... N^2

# Even from just the first three terms, we can see that P_N grows very fast. At which NN is P_N 1000 times greater than NN for the first time? (In other words, when does the total number of bricks become more than 1000 times the number of bricks along an edge?)

s = 0
for N in range(100):
    s = s + N**2
    print(N, s - 1000*N)

# One possibility is to list N, P_N, and 1000N and to look for the first entry where P_N > 1000N. It becomes a little easier to parse if we list N and P_N-1000N and look for the first positive entry in the second row.