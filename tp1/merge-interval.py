def fusionner_intervalles(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    resultat = [intervals[0]]
    
    for debut, fin in intervals[1:]:
        dernier_debut, dernier_fin = resultat[-1]
        
        if debut <= dernier_fin:
            resultat[-1][1] = max(dernier_fin, fin)
        else:
            resultat.append([debut, fin])
    
    return resultat


intervalles = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Intervalles fusionnés :", fusionner_intervalles(intervalles))
# Intervalles fusionnés : [[1, 6], [8, 10], [15, 18]]