import codecs
from marketingbot.loader import db


FILE_NAME = 'phraselist.txt'
CATEGORY = 'neutral'

file = codecs.open(FILE_NAME, "r", "utf_8_sig")

for line in file:
    db.phrase_add(phrase=line, category=CATEGORY)

print('ready!')