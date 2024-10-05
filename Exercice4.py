import re

print("akinalf tg !!!!!!")

file_sms = open("SMSSpamCollection.tsv", "r")

# Remplacer tous les caractères non alphabétiques par des espaces
def preprocess(text):
    processed_text = re.sub(r'[^a-zA-Z]', ' ', text)
    processed_text = re.sub('  +', ' ', processed_text)
    return processed_text

def categorize_spam(file_sms):
  line = file_sms.readline()
  spam = []
  ham = []
  while line != "":
    if line[0:4] == "spam":
      spam.append(line)
    elif line[0:3] == "ham":
      ham.append(line)
    else : print("Ligne ni spam, ni ham: ", {line})
    line = file_sms.readline()

  return spam, ham

spam, ham = categorize_spam(file_sms)

mega_document = str(spam) + ' ' + str(ham)

token_spam = str(spam).split()
token_ham = str(ham).split()




#print(len(spam), len(ham))
#print (len(mega_document))

text = "coucou La Mi/FF !!! J'éspère vous allez iennnbùùù :)"

tab = preprocess(text).split(' ')

print (tab)







