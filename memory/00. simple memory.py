
"""
1. Chat Prompt
2. Chat Template
3. Chain
4. Sequential Chain
5. Memory
"""
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import  StrOutputParser
from langchain_groq import ChatGroq


# Load the environment variables
load_dotenv()

# Initialize the LLM
model = "llama-3.3-70b-versatile"
llm = ChatGroq(model=model)

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="Write a short story (100-150 words) based on the given plot and past message histories.."),
    MessagesPlaceholder(variable_name="history"),
])

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

history = []

while True:
    input_text = input("You: ")

    if input_text.strip() == 'exit':
        break
    history.append(HumanMessage(content=input_text))

    # Run the chain
    response = chain.invoke(history)
    history.append(AIMessage(content=response))

    print(f"Bot: {response}")

    print(history)
