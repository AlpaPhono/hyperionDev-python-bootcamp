# ============ Working with the spacy ============== # 
import spacy


nlp = spacy.load("en_core_web_sm")
#=========================================
# Create a list called gardenpathSentences 
#=========================================

gardenpathSentences = [
    "The old man the boat",
    "The complex houses married and single soldiers and their families",
    "The horse raced past the barn fell",
    "The cotton clothing is made of grows in Mississippi",
    "Have the students who failed the exam take the supplementary"
]

#========================================
# Tokenise each sentence in the list and
# perform entity recognition 
# =======================================

for line in gardenpathSentences:
    doc = nlp(line)
    print([(token, token.orth_, token.orth) for token in doc])
