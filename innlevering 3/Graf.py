Graf = {}

a_filnavn = input("Skuespillere: ")
m_filnavn = input("Filmer: ")
filmer = set()
skuespillere = set()
print("\n")

with open(m_filnavn, "r") as fil:
    for line in fil:
        deler = line.split()
        film = deler[0]
        Graf[film] = [deler[1], deler[2]]
        

with open(a_filnavn, "r") as fil:
    for line in fil:
        deler = line.split()
        skuespillere = deler[0]
        navn = deler[1]
        filmer = [f for f in deler[2:] if f in Graf]
        Graf[skuespillere] = filmer
