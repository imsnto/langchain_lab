from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory # deprecated
from langchain.chains import ConversationChain, LLMChain # deprecated
from langchain.prompts import ChatPromptTemplate

# Load the environment variables
load_dotenv()

# Initialize the LLM
model = "llama-3.3-70b-versatile"
llm = ChatGroq(model=model)

# Memory
memory = ConversationBufferMemory(memory_key="chat_history")

memory.save_context({"input": "hi"}, {"output": "hello"})
memory.save_context({"input": "hey"}, {"output": "hellooo"})

print(memory.load_memory_variables({}))

# history as a list of messages
memory = ConversationBufferMemory(return_messages=True)
memory.save_context({"input": "hi"}, {"output": "whats up"})

print(memory.load_memory_variables({}))

template = """You are a nice chatbot having a conversation with a human.
    Previous conversation:
    {chat_history}

    New human question: {question}
    Response:
    """
prompt = ChatPromptTemplate.from_template(template)

# Chain

# conversation = LLMChain(
#     llm=llm,
#     prompt=prompt,
#     verbose=True,
#     memory=ConversationBufferMemory(memory_key="chat_history")
# )


print(prompt.input_variables)
conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferMemory(memory_key="chat_history"),
    input_key="question"
)

while True:
    input_text = input("You: ")
    if input_text.strip() == 'exit':
        break
    response = conversation({"question": input_text})
    print(f"Bot: {response['response']}")
    # response = conversation({"input": input_text}) print(f"Bot: {response}")
