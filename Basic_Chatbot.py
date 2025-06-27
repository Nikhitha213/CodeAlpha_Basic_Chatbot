def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! 👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks! 😊 How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! 👋 Have a great day!"
    elif "your name" in user_input:
        return "I'm ChatBot 101, your friendly assistant!"
    elif "help" in user_input:
        return "You can say hello, ask how I am, or say goodbye."
    else:
        return "Sorry, I don't understand that yet. 😅"

# Main loop
print("🤖 ChatBot 101: Type 'bye' to exit.")
while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Bot:", response)
    if "bye" in user.lower():
        break