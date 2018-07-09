import nltk
import requests
import json

app_id = 'e0876eb7'
app_key = '2b9f1d46348eb2ba04ebca49c03b54b7'

language = 'en'


f = open('melville.txt','r')
lines = f.read()
sentences = nltk.sent_tokenize(lines) #tokenize sentences

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if pos.startswith('NN'):
             url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()
             r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
             print("json \n" + json.dumps(r.json()))
