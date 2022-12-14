import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('SMS - EMAIL SPAM 🚫 CLASSIFIER')
st.image('spam.jpg')
input = st.text_area('ENTER THE MESSAGE 📧✉️')


def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  y = []
  for i in text:
     if i.isalnum():
       y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return ' '.join(y)


if st.button('PREDICT 🔽'):
  # 1. PREPROCESSING
  transformed_text = transform_text(input)

  # 2. VECTORIZATION
  vector_input = tfidf.transform([transformed_text])

  # 3. PREDICTION
  result = model.predict(vector_input)[0]

  # 4. DISPLAY
  if result == 1:
      st.header('🥴🥴🥴SPAM🥴🥴🥴')
  else:
      st.header('🥳🥳🥳NOT A SPAM 🥳🥳🥳')