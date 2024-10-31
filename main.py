import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": ["Hello!", "Hi there!", "Greetings!"],
            "how are you?": ["I'm just a program, but thanks for asking!", "Doing well, how about you?", "I don't have feelings, but I'm here to help!"],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "default": ["I'm not sure how to respond to that.", "Can you tell me more?", "Let's talk about something else."],
            "give me information about reading books": ["well reading book make you smart enouth"],
            "israil": ["non contury", "do you mean bani israil?"],
            "fuck": ["fuck you to "],
            "spiderman": ["spiderman is a old superhero was existed in comic by stanlee from marvel studio"],
            "chatgpt": ["chatgpt is one of the famous ai in the intenet history"],
            "algeria": ["algeria is one of the biggest muslim contury in world", "algeria is a old contury that existed in 1800s"],
            "how to be a pro student": ["1-revive the lessons every day, 2-remeber the word you learn, 3-you have to work your homework every day"],
            "tell me more about algeria": ["algeria has a beutifull places: 1-bjaia, 2-batna, 3-algeria, 4-telemcan"],
            "samsung or iphone": ["Samsung might be your best choice if you value advanced camera technology, extensive customization, and cutting-edge display capabilities. For users who prioritize a streamlined user experience, robust data security, and tight integration across devices, Apple stands out as the top option."],
            
        }

    def get_response(self, user_input):
        # Normalize the input to lower case
        user_input = user_input.lower()
        # Return a random response from the matched category or a default response
        return random.choice(self.responses.get(user_input, self.responses["default"]))

def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    bot = SimpleChatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
