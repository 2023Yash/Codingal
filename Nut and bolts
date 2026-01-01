def nuts_bolts(nuts, bolts):
    n = len(nuts)
    matched_bolts = [None] * n
    
    for i in range(n):
        for j in range(n):
            if nuts[i] == bolts[j]:
                matched_bolts[i] = bolts[j]
                break
    return matched_bolts

nuts= [4, 2, 5, 1, 3]
bolts = [1, 5, 3, 2, 4]

matched = nuts_bolts(nuts, bolts)