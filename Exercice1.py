import tqdm

def main():
    
    word = input("le mot: ")
    best_distance, closest_words = find_closest_words(word)

    print(best_distance)
    print(closest_words)


def get_min_around(grille, i, j, mot1, mot2):
    gauche = grille[i][j-1] + 1
    diag_haut_gauche = grille[i-1][j-1]
    haut = grille[i-1][j] + 1

    if(len(mot1) - i) < 0 or (len(mot2) - j) <0 or (mot1[j-1] != mot2[i-1]):
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
    #affichage(grille)
    return grille[len(mot2)][len(mot1)]

#print(levenshtein("antépénultièmeàtagrandmèrelatainp", "antérieuràtongrospere"))


def find_closest_words(word):
    with open("french.txt", "r") as file:
        dictionary_words = file.readlines()
    
    closest_words = []
    best_distance = float('inf')

    for dictionnary_word in tqdm.tqdm(dictionary_words, desc="Processing words"):
        dictionnary_word = dictionnary_word.strip()
        distance = levenshtein(word, dictionnary_word)
        if distance < best_distance:
            best_distance = distance
            closest_words = [dictionnary_word]
        elif distance == best_distance:
            closest_words.append(dictionnary_word)

    return best_distance, closest_words

if __name__ == "__main__":
    main()


# def find_closest_words(word):
#     file = open("french.txt", "r")
#     dictionnary_word = file.readline()
#     closest_words = [dictionnary_word]
#     best_distance = levenshtein(word, dictionnary_word)
#     dictionnary_word = file.readline()
    
#     while dictionnary_word != "" :
#         distance = levenshtein(word, dictionnary_word)
#         if distance < best_distance:
#             best_distance = distance
#             closest_words = [dictionnary_word]
#         elif distance == best_distance:
#             closest_words.append(dictionnary_word)
        
#         dictionnary_word = file.readline()

#     return best_distance, closest_words



# main()