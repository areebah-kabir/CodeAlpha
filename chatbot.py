import nltk
from nltk.chat.util import Chat, reflections

# Pairs of inputs and responses
pairs = [
    ['hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am fine, thank you!', 'I am doing well, and you?']],
    ['what is your name?', ['I am a chatbot. What’s yours?']],
    ['goodbye|bye', ['Goodbye!', 'See you later!']]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot
if __name__ == "__main__":
    print("Chatbot: Hi, I am your friendly chatbot. Type something to start chatting!")
    chatbot.converse()
