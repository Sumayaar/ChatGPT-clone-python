from dotenv import load_dotenv
import os
##stores history of your chats so that LLM has all the context of your previouse responses
from langchain.chat_models import ChatOpenAI ##wrapper for the OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

#first message we are giving to LLM the instructions how it is supposed to act, 
# second one is our message which contains our question
# thrid one is the response from AI model

    
def main():
    load_dotenv()

    # test our API key
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI API key is not set, please add the key")
        exit(1)
    else:
        print("API key is set.")

    llm = ChatOpenAI(temperature=0.4)
    conversation = ConversationChain(llm= llm, 
                                     memory=ConversationBufferMemory(),
                                     verbose=True
                                     )

    print('hello, I am ChatGPT CLI')

    while True:
        user_input=input(">>")
        
        ai_response = conversation.predict(input=user_input)
        print("\n Assistant: \n", ai_response)
       
    

if __name__ == '__main__':
    main()

