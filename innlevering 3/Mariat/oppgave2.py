
from buildGraf import alt_dict
#alt_dit representerer grafen og inneholder nodet, kanter og vektene

def DFS(s, visited):  # DFS med stack
    resultat = []
    stack = [s]

    while stack:
        u = stack.pop()
        if u not in visited:
            resultat.append(u)
            visited.add(u)
            
            for v in alt_dict[u]:
                if v not in visited:
                    stack.append(v)
    return resultat



def kompSize():
    visited = set()
    size = []

    # Bygg mengden av noder fra både nøkler og naboer
    V = set(alt_dict.keys())

    for i in alt_dict.values():
        for v in i:
            V.add(v)

    for v in V:
        if v not in visited:
            comp = DFS(v, visited)
            size.append(len(comp))
    return size



def skrivStørrelser():
    size = kompSize()
    freq = {}
    for i in size:
        freq[i] = freq.get(i, 0) + 1
    for i in freq:
        print("There are", freq[i], "components of size", i)

skrivStørrelser()