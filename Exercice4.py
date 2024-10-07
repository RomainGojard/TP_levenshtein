import re
from collections import Counter
from sklearn.model_selection import train_test_split

# Q4 à Q6 : Prétraitement
def preprocess(text):
    processed_text = re.sub(r'[^a-zA-Z]', ' ', text)
    processed_text = re.sub('  +', ' ', processed_text)
    return processed_text.lower()

# Q1 : Lecture du fichier et séparation en spam et ham
def categorize_spam(file_sms):
    spam, ham = [], []
    for line in file_sms:
        line = line.strip()
        label, message = line.split('\t')
        if label == "spam":
            spam.append(preprocess(message))
        elif label == "ham":
            ham.append(preprocess(message))
    return spam, ham

# Q7 et Q8 : Entraînement du classifieur bayésien
def bayes_train(spam, ham):
    spam_text = ' '.join(spam)
    ham_text = ' '.join(ham)
    spam_tokens = spam_text.split()
    ham_tokens = ham_text.split()
    vocabulary = set(spam_tokens + ham_tokens)
    spam_counts = Counter(spam_tokens)
    ham_counts = Counter(ham_tokens)
    return vocabulary, spam_counts, ham_counts, len(spam_tokens), len(ham_tokens)

# Q10 : Calcul de P(wi|cj)
def prob_word(word, class_counts, total_words, vocab_size, alpha=1):
    return (class_counts[word] + alpha) / (total_words + alpha * vocab_size)

# Q11 : Calcul de P(c|d)
def prob_class(tokens, class_counts, total_words, vocab_size):
    prob = 0
    for token in tokens:
        prob += prob_word(token, class_counts, total_words, vocab_size)
    return prob

# Q12 : Prédire si un SMS est un spam
def is_spam(sms, vocabulary, spam_counts, ham_counts, total_spam_words, total_ham_words):
    tokens = preprocess(sms).split()
    spam_prob = prob_class(tokens, spam_counts, total_spam_words, len(vocabulary))
    ham_prob = prob_class(tokens, ham_counts, total_ham_words, len(vocabulary))
    return "spam" if spam_prob > ham_prob else "ham"

# Q14 à Q16 : Évaluation du classifieur
def evaluate(spam_test, ham_test, vocabulary, spam_counts, ham_counts, total_spam_words, total_ham_words):
    correct = 0
    total = len(spam_test) + len(ham_test)
    for sms in spam_test:
        if is_spam(sms, vocabulary, spam_counts, ham_counts, total_spam_words, total_ham_words) == "spam":
            correct += 1
    for sms in ham_test:
        if is_spam(sms, vocabulary, spam_counts, ham_counts, total_spam_words, total_ham_words) == "ham":
            correct += 1
    return correct / total

# Lecture du fichier
file_sms = open("SMSSpamCollection.tsv", "r")

# Q1 : Séparation en spam et ham
spam, ham = categorize_spam(file_sms)

# Q2 : Comptage des SMS
print(f"Nombre de spams : {len(spam)}")
print(f"Nombre de hams : {len(ham)}")

# Q2 : Probabilité d'avoir un spam
total_sms = len(spam) + len(ham)
prob_spam = len(spam) / total_sms
print(f"Probabilité d'avoir un spam : {prob_spam}")

# Q14 : Division en ensemble d'entraînement (75%) et de test (25%) avec sklearn
spam_train, spam_test = train_test_split(spam, test_size=0.25, random_state=42)
ham_train, ham_test = train_test_split(ham, test_size=0.25, random_state=42)

# Q7 à Q9 : Entraînement
vocabulary, spam_counts, ham_counts, total_spam_words, total_ham_words = bayes_train(spam_train, ham_train)

# Q15 et Q16 : Taux de succès
success_rate = evaluate(spam_test, ham_test, vocabulary, spam_counts, ham_counts, total_spam_words, total_ham_words)
print(f"Taux de succès du classifieur : {success_rate * 100:.2f}%")
