print("akinalf tg !!!!!!")

file_sms = open("SMSSpamCollection.tsv", "r")


def categorize_spam(file_sms):
  line = file_sms.readline()
  spam = []
  ham = []
  while line != "":
    if line[0:4] == "spam":
      spam.append(line)
    elif line[0:3] == "ham":
      ham.append(line)
    else : print("erreur, ligne chelou sa mère la tainp")
    line = file_sms.readline()

  return spam, ham

spam, ham = categorize_spam(file_sms)

print(spam.count)