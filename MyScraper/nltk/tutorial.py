from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
a = set(stopwords.words('english'))


st = "This will load the image or iFrame straight away. This is the same as not having a loading attribute so we won't be using it.".lower()

# To filter out stop words
tk = word_tokenize(st)
filtered_ls = [w for w in tk if w not in a]
print(filtered_ls)

# to get V1 form or stem
from nltk.stem import LancasterStemmer
# Lancaster Stemmer
# Snowball stemmer
ps = LancasterStemmer()

for i in filtered_ls:
    print(ps.stem(i))
