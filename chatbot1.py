from google import genai

client=genai.Client(api_key="API KEY")
chat=client.chats.create(model="gemini-2.5-flash")

print("Chatbot ready! Type 'quit' to exit")
print("-" * 30)

while True:
    user_input=input("You:")

    if user_input.lower()=="quit":
        print("Bye!")
        break
    response=chat.send_message(user_input)
    print("Bot:", response.text)
    print()

