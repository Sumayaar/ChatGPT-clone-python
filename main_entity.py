from dotenv import load_dotenv
import os
##stores history of your chats so that LLM has all the context of your previouse responses
from langchain.chat_models import ChatOpenAI ##wrapper for the OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

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
    #we are passing  llm to conversation entity memory because it requires llm to
    #  generate the entities inside of it and to remember the entities inside the conversation
    conversation = ConversationChain(llm= llm, 
                                     memory=ConversationEntityMemory(llm=llm),
                                     prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
                                     verbose=True
                                     )

    print('hello, I am ChatGPT CLI')

    while True:
        user_input=input(">>")
        
        ai_response = conversation.predict(input=user_input)
        print("\n Assistant: \n", ai_response)
       
    

if __name__ == '__main__':
    main()

