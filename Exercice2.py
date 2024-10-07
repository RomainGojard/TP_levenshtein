import tqdm
from queue import PriorityQueue

def main():
    word = input("le mot: ")
    best_distance, closest_words = find_closest_words(word)

    print(best_distance)
    print(closest_words)


def get_min_around(grille, i, j, mot1, mot2):
    gauche = grille[i][j-1] + 1  # Suppression
    diag_haut_gauche = grille[i-1][j-1]  # Substitution ou correspondance
    haut = grille[i-1][j] + 1  # Insertion

    isSameCharacter = True

    if mot1[j-1] != mot2[i-1]:
        diag_haut_gauche += 2  # Substitution
        isSameCharacter = False

    if diag_haut_gauche <= gauche and diag_haut_gauche <= haut:
        if isSameCharacter:
            chemin = "-"  # Correspondance
        else:
            chemin = "S"  # Substitution
    elif gauche <= haut:
        chemin = "D"  # Suppression
    else:
        chemin = "I"  # Insertion

    return min(gauche, diag_haut_gauche, haut), chemin


def affichage(grille):
    for i in range(len(grille)):
        print(grille[i])


def reconstituer_chemin(grille_chemin, mot1, mot2):
    i, j = len(mot2), len(mot1)
    chemin = []
    
    # On part de la dernière case et on remonte
    while i > 0 or j > 0:
        operation = grille_chemin[i][j]
        chemin.append(operation)
        if operation == "S" or operation == "-":
            i -= 1
            j -= 1
        elif operation == "D":
            j -= 1
        elif operation == "I":
            i -= 1
    
    chemin.reverse()  # On remet le chemin à l'endroit
    return chemin


def levenshtein(mot1, mot2):
    grille = [[0] * (len(mot1) + 1) for _ in range(len(mot2) + 1)]
    grille_chemin = [[""] * (len(mot1) + 1) for _ in range(len(mot2) + 1)]

    for i in range(len(grille)):
        for j in range(len(grille[i])): 
            if i == 0:
                grille[i][j] = j 
                grille_chemin[i][j] = "D" if j > 0 else ""  
            elif j == 0:
                grille[i][j] = i 
                grille_chemin[i][j] = "I" if i > 0 else "" 
            else:
                grille[i][j], grille_chemin[i][j] = get_min_around(grille, i, j, mot1, mot2)

    affichage(grille_chemin)

    chemin = reconstituer_chemin(grille_chemin, mot1, mot2)

    return grille[len(mot2)][len(mot1)], chemin


def find_closest_words(word):
    with open("french.txt", "r") as file:
        dictionary_words = file.readline()
    
    closest_words = []
    best_distance = float('inf')

    for dictionnary_word in tqdm.tqdm(dictionary_words, desc="Processing words"):
        dictionnary_word = dictionnary_word.strip()
        distance, _ = levenshtein(word, dictionnary_word)  # On ne garde que la distance
        if distance < best_distance:
            best_distance = distance
            closest_words = [dictionnary_word]
        elif distance == best_distance:
            closest_words.append(dictionnary_word)

    return best_distance, closest_words


# Test
distance, chemin = levenshtein("completement", "compliment")
print(f"Distance: {distance}")
print(f"Chemin: {chemin}")
