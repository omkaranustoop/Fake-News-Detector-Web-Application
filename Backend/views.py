from django.http import HttpResponse
from django.shortcuts import render
from keras.models import load_model
from bs4 import BeautifulSoup
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import joblib
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import pickle
from django.http import JsonResponse


replace_by_space = re.compile('[/(){}\[\]\|@,;]')
replace_symbol = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))
STOPWORDS.add('India')
STOPWORDS.add('india')

def string_form(value):
    return str(value)

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").text # HTML decoding
    text = text.lower() # lowercase text
    text = replace_by_space.sub(' ', text) # replace certain symbols by space in text
    text = replace_symbol.sub('', text) # delete symbols from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove STOPWORDS from text
    return text

data = pd.read_csv('fake.csv')
X_data = data['text'] + data['title']

X_data = X_data.apply(string_form)
X_data = X_data.apply(clean_text)
X_data_final = []

for e in range(len(X_data)):
    if(X_data[e] != 'nan'):
       X_data_final.append(X_data[e])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_data_final)
all_words = []
for word, index in tokenizer.word_index.items():
    all_words.append(word)
    
all_words.sort()


def home(request):
    return render(request,"home.html")

def find(s,words):
    l = 0
    r = len(words)-1
    while l <= r:
        mid = l + (r-l)//2
        if words[mid] == s:
            return True
        else:
            if words[mid] > s:
                r = mid-1
            else:
                l = mid+1
    return False

def result(request):

#   model = pickle.load(open("Final_Model2.sav", "rb"))
    model = load_model('my_model7.h5') 

    input = request.body
    input = clean_text(str(input));
    
    text1 = input.split()
    text = []
    for e in range(len(text1)):
        if e < 1500 and find(text1[e], all_words):
            text.append(text1[e])
        elif e >= 1500:
            break
    final_text = ""
    for e in text:
        final_text += ' '
        final_text += e

    data_final = []
    data_final.append(final_text)

    encoded_text = tokenizer.texts_to_sequences(data_final)
    X = pad_sequences(encoded_text, maxlen = 1500, padding = 'post')
  
    y_pred = model.predict([X])
    ans = y_pred[0]
    felina = ans[0]*100

    if len(text) < 50:
        felina = "'Too Small!!! Length should be more than 50 words'"

    return JsonResponse({'score':felina})