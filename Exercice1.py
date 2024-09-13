import tqdm
from queue import PriorityQueue

def main():
    word = input("le mot: ")
    closest_words = find_closest_words(word)

    print("Les 10 mots les plus proches sont :")
    for distance, closest_word in closest_words:
        print(f"{closest_word.strip()} avec une distance de {-distance}")

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
    
    pq = PriorityQueue()

    for dictionary_word in tqdm.tqdm(dictionary_words, desc="Processing words"):
        dictionary_word = dictionary_word.strip()
        distance = levenshtein(word, dictionary_word)
        
        pq.put((-distance, dictionary_word)) 
        
        if pq.qsize() > 10:
            pq.get()

    closest_words = []
    while not pq.empty():
        closest_words.append(pq.get())

    return closest_words

if __name__ == "__main__":
    main()