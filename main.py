## stemming
nltk.download('stopwords')

for i in corpus :

  words = nltk.word_tokenize(i)
  for word in words:
    if word not in set(stopwords.words('english')):
      print(stemmer.stem(word))
