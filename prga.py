# E1E120024
# AFDHALUL RAHMAT SEPTYO


S = list(range(256))
i = 0
j = 0
P = "2024"
print("hasil enkripsi: ", end="")
for idx in range(len(P)-1):
    i = (i+1) % 256
    j = (j+S[i]) % 256
    S[i], S[j] = S[j], S[i]
    t = (S[i] + S[j]) % 256
    u = S[t]
    c = u ^ ord(P[idx])
    print(chr(c), end="")
print("\narray: ", S)
