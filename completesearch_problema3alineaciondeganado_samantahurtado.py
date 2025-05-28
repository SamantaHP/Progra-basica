import itertools

#lista fija de vacas
cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
#lista de restricciones
restrictions = [("Buttercup", "Bella"), ("Blue", "Bella"), ("Sue", "Beatrice")]
#funcion para verificar si una permutacion satisface todas las restricciones
def is_valid_order(order, restrictions):
    for cow1, cow2 in restrictions:
        idx1 = order.index(cow1)
        idx2 = order.index(cow2)
        if abs(idx1 - idx2) != 1:
            return false
    return true
#buscar la permutacion valida mas antigua alfabeticamente
for perm in sorted (itertools.permutations(cows)):
    if is_valid_order(perm, restrictions):
        for cow in perm:
            for cow in perm:
                print (cow)
            break
        
