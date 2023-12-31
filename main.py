from dotenv import load_dotenv
import os
##stores history of your chats so that LLM has all the context of your previouse responses
from langchain.chat_models import ChatOpenAI ##wrapper for the OpenAI

#first message we are giving to LLM the instructions how it is supposed to act, 
# second one is our message which contains our question
# thrid one is the response from AI model

from langchain.schema import(
            SystemMessage,
            HumanMessage,
            AIMessage
)
    
def main():
    load_dotenv()

    # test our API key
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI API key is not set, please add the key")
        exit(1)
    else:
        print("API key is set.")

    chat = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")
    #array of all our messages
    messages = [
        SystemMessage(content="You are an helpful assistant"),
        
    ]

    print('hello, I am ChatGPT CLI')

    while True:
        user_input=input(">>")
        # print("you sent: ", user_input)
        #appending to messages
        messages.append(HumanMessage(content=user_input))

        ##generate our response
        ai_response = chat(messages)

        messages.append(AIMessage(content=ai_response.content))
        print("\n Assistant: \n", ai_response.content)
        print("History :", messages)
    

if __name__ == '__main__':
    main()