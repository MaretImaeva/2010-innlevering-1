from graf1000 import alt_dict

def DFS(s, visited):  
    resultat = []
    stack = [s]

    while stack:
        u = stack.pop()
        if u not in visited:
            resultat.append(u)
            visited.add(u)
            for v, film_tittel, film_id, rating in alt_dict.get(u, {}).get("kant", []):
                if v not in visited:
                    stack.append(v)
    return resultat

# Finner størrelsen på komponentene
def kompSize(): 
    visited = set()
    size = []
    V = set(alt_dict.keys())
    for entry in alt_dict.values():
        for v_id, film_tittel, film_id, rating in entry.get("kant", []):
            V.add(v_id)

    for v in V:
        if v not in visited:
            comp = DFS( v, visited)
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



