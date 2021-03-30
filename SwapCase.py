import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
S = raw_input()

T = []
for i in range(len(S)):
    if S[i] in lower:
        T.append(S[i].upper())
    elif S[i] in upper:
        T.append(S[i].lower())
    else:
        T.append(S[i])
print ''.join(T)
