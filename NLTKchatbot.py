#pip install nltk 

import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# define a dictionary with intents and responses
intents = {
    "hello": "Hi, how can I help you?",
    "bye": "Goodbye, have a great day!",
    "thanks": "You're welcome!",
    "help": "I can assist you with questions or tasks."
}

# function to process user input
def process_input(input_text):
    input_text = input_text.lower()
    words = nltk.word_tokenize(input_text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

# function to find a matching intent
def find_intent(words):
    for intent, response in intents.items():
        if all(word in words for word in intent.split()):
            return response
    return "Sorry, I didn't understand that."

# main chatbot loop
while True:
    user_input = input("You: ")
    words = process_input(user_input)
    response = find_intent(words)
    print("Chatbot:", response)


