import subprocess as sp
import nltk
import warnings
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


warnings.filterwarnings("ignore")

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "whats up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
LEMER = nltk.stem.WordNetLemmatizer()


def lematize_tokens(tokens):
    return [LEMER.lemmatize(token) for token in tokens]


def lematization_normalizer(text):
    return lematize_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    robo_response=''
    sentence_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=lematization_normalizer, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sentence_tokens[idx]
        return robo_response


with open("myresume", "r", errors="ignore") as f:
    raw = f.read().lower()
    nltk.download('punkt')  # first-time use only
    nltk.download('wordnet')  # first-time use only
    sentence_tokens = nltk.sent_tokenize(raw)
    word_tokens = nltk.word_tokenize(raw)
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    flag = True
    tmp = sp.call('cls',shell=True)
    print('************************************** MyResume Chatbot By Anil ********************************')
    print("MyResume-BOT: Hi! My name is Anil. I will try to answer most of your queries related to my resume. If you want to exit, type Bye!")
    while (flag == True):
        print("You: ", end="")
        user_response = input()
        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                print("BNU-BOT: You are welcome..")
            else:
                if (greeting(user_response) != None):
                    print("MyResume-BOT: " + greeting(user_response) + "\n")
                else:
                    print("MyResume-BOT: ", end="")
                    print(response(user_response)  + "\n")
                    sentence_tokens.remove(user_response)
        else:
            flag = False
            print("MyResume-BOT: Bye! take care..")
