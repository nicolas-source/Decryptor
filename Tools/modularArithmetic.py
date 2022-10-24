import math

superIncreasing_knapsack = [2, 3, 6, 13, 27, 52]

general_knapsack = []

m = 31
n = 105

for i in superIncreasing_knapsack:
    general_knapsack_element = i * m % n
    general_knapsack.append(general_knapsack_element)

print("KNAPSACK")
print("public key: =", general_knapsack)

print("private key: =", superIncreasing_knapsack)
print("m: ", m)
print("n: ", n)

# (m^-1 mod n) == M^-1
print(pow(m, -1, n))

print("---------------------")
print("RSA")
M = 4
e = 3
Alice_N = 147
Alice_d = 103
Bob_N = 55
Bob_d = 27

C = pow(M, e) % Bob_N


print(C)


print(math.log(2,10))