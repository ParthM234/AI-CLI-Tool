from google import genai

client=genai.Client(api_key="API KEY")

def TextSummarizer(text):
    prompt = f"Summarize this in 3-5 bullet points:\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def sentiment(text):
    prompt= f"Analyse the sentiment of this sentence.Say if it is Positive, Negative or Neutral and explain why in 2 lines:\n{text}"
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
 
def chat():
    conversation=client.chats.create(model="gemini-2.5-flash")
    print("Chat mode - type 'back' to move to menu")
    while True:
        user_input=input("You:")
        
        if user_input.lower()=="back":
            break
        response= conversation.send_message(user_input)
        print("Bot:", response.text)

def answer(question):
        prompt = f"Answer this question clearly and concisely in 3-5 lines:\n{question}"
        response = client.models.generate_content(
             model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text

def main():
    print("AI Tool")
    print("-"*30)

    while True:
        print("\n1. Summarize text")
        print("2. Sentiment analysis")
        print("3. Chat")
        print("4. Ask a Question")
        print("5. Quit")
        
        choice = input("\nChoose (1-4): ")

        if choice=="1":
            lines=[]
            while True:
                line=input()
                if line=="":
                    break
                lines.append(line)
            print("\n Summary")
            print(TextSummarizer("\n".join(lines)))

        elif choice =="2":
            text=input("Enter text: ")
            print("\n Sentiment")
            print(sentiment(text))

        elif choice=="3":
            chat()

        elif choice=="4":
            question= input("Ask any question!")
            print("\nAnswer:")
            print(answer(question))

        elif choice== "5":
            print("Bye!")
            break

main()    

