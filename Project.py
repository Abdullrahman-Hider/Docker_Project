import re 
import nltk 
from nltk.corpus import stopwords
nltk.download('stopwords')


with open("random_paragraphs.txt") as file:
    text = file.read()
 

words_list = re.split(r'[ \n.,;!?"]+', text)
words_list = words_list[:-1]


stop_words = stopwords.words('english')

filtered_list = [word for word in words_list if word.lower() not in stop_words]


words_freqs = {}
for word in filtered_list:
    if word in words_freqs.keys():
        words_freqs[word]+=1
    else:
        words_freqs[word]=1
        
print('Number of unique words: ', len(words_freqs))


# - Displaying the word frequencies
top_words = [word for word in words_freqs.keys() if words_freqs[word]>400]
for word in top_words:
    print(f'{word}: {words_freqs[word]}')