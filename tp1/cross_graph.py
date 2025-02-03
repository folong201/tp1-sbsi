from collections import deque

def bfs(graphe, depart):
    visite = set()
    file = deque([depart])
    resultat = []
    
    while file:
        noeud = file.popleft()
        if noeud not in visite:
            visite.add(noeud)
            resultat.append(noeud)
            file.extend(graphe[noeud])
    
    return resultat

def dfs(graphe, depart, visite=None):
    if visite is None:
        visite = set()
    visite.add(depart)
    
    for voisin in graphe[depart]:
        if voisin not in visite:
            dfs(graphe, voisin, visite)
    
    return visite

def chemin_plus_court(graphe, depart, cible):
    file = deque([(depart, [depart])])
    
    while file:
        noeud, chemin = file.popleft()
        for voisin in graphe[noeud]:
            if voisin == cible:
                return chemin + [voisin]
            if voisin not in chemin:
                file.append((voisin, chemin + [voisin]))
    return None

graphe = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

print("Parcours BFS :", bfs(graphe, 'A'))
print("Parcours DFS :", dfs(graphe, 'A'))
print("Chemin le plus court de A à F :", chemin_plus_court(graphe, 'A', 'F'))