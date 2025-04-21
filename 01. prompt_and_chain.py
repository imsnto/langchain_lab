"""
1. Chat Prompt
2. Chat Template
3. Chain
4. Sequential Chain
5. Memory
"""
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import  StrOutputParser
from langchain_groq import ChatGroq

# Load the environment variables
load_dotenv()

# Initialize the LLM
model = "llama-3.3-70b-versatile"
llm = ChatGroq(model=model)

# Create a template
template = """
    Write a short story (100-150 words) about this context: {context} 
"""

# Create a prompt using this template
prompt = ChatPromptTemplate.from_template(template=template)

# Create output parse
output_parser = StrOutputParser()

# Create a chain
chain1 = prompt | llm | output_parser

template2 = """
    Translate this story into bengali: {story}
"""
prmpt2 = ChatPromptTemplate.from_template(template=template2)
chain2 = prmpt2 | llm | output_parser

# Sequential chain
chain = chain1 | chain2 | output_parser

while True:
    context = input("Bot: ")

    if context.strip() == 'exit':
        break

    inputs = {
        "context": context
    }
    # Run the chain
    response = chain.invoke(inputs)
    print(f"Bot: {response}")



