print("ARTTIFAI TECH")
print("Let's chat! Type 'quit' to exit\n")

#  Predefined keyword-based responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there, how can I help?",
    "name": "I'm a simple Python chatbot!",
    "coffee": "We have coffee and tea.",
    "tea": "We have coffee and tea.",
    "credit card": "We accept most major credit cards, and Paypal.",
    "paypal": "We accept most major credit cards, and Paypal.",
    "thank": "Happy to help!",
    "bye": "Goodbye! Have a great day.",
}

def get_response(message):
    msg = message.lower()
    for keyword, reply in responses.items():
        if keyword in msg:
            return f"Bot: {reply}"
    return "Bot: I'm not sure how to respond to that."

#  Main loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print(response)