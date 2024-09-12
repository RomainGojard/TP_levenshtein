import tqdm

def main(mot):
    mot2 = "apagnan"
    levenshtein(mot, mot2)
    return mot


def get_min_around(grille, i, j, mot1, mot2):
    gauche = grille[i][j-1] + 1
    diag_haut_gauche = grille[i-1][j-1]
    haut = grille[i-1][j] + 1

    if(len(mot1) - i) < 0 or (len(mot2) - j) <0 or (mot1[i-1] != mot2[j-1]):
        diag_haut_gauche += 2
    return min(gauche, diag_haut_gauche, haut)



def affichage(grille):
    for i in range(len(grille)) :
        print(grille[i])
        
        
def levenshtein(mot1, mot2):
  
    grille = [[0] * (len(mot1) + 1) for _ in range(len(mot2) + 1)]

    for i in range(len(grille)): # chaque ligne
        for j in range(len(grille[i])): # chaque colonne
            if(i == 0):
                grille[i][j] = j 
            elif(j == 0):
                grille[i][j] = i
            else:
                grille[i][j] = get_min_around(grille, i, j, mot1, mot2)


    #print(grille)
    affichage(grille)
    return grille[len(mot1)][len(mot2)]

print(levenshtein("dragon", "drogu"))
