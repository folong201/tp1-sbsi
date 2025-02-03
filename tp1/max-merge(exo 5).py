def fusionner_intervalles(intervalles):
    if not intervalles:
        return []
    
    intervalles.sort(key=lambda x: x[0])
    resultat = [intervalles[0]]
    
    for debut, fin in intervalles[1:]:
        dernier_debut, dernier_fin = resultat[-1]
        
        if debut <= dernier_fin:  # Fusion
            resultat[-1] = (dernier_debut, max(dernier_fin, fin))
        else:
            resultat.append((debut, fin))
    
    return resultat



intervalles = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Intervalles fusionnés :", fusionner_intervalles(intervalles))
# Intervalles fusionnés : [[1, 6], [8, 10], [15, 18]]