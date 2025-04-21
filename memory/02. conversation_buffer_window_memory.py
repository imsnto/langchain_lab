from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferWindowMemory # deprecated
from langchain.chains import ConversationChain # deprecated

# Load the environment variables
load_dotenv()

# Initialize the LLM
model = "llama-3.3-70b-versatile"
llm = ChatGroq(model=model)

# Memory
#  It only uses the last K interactions.
memory = ConversationBufferWindowMemory(k=2)

memory.save_context({"input": "hi"}, {"output": "hello"})
memory.save_context({"input": "hey2"}, {"output": "hellooo2"})
memory.save_context({"input": "hey3"}, {"output": "hellooo3"})

print(memory.load_memory_variables({}))

# history as a list of messages
memory = ConversationBufferWindowMemory(k=2, return_messages=True)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "hi2"}, {"output": "whats up2"})
memory.save_context({"input": "hi3"}, {"output": "whats up3"})

print(memory.load_memory_variables({}))

# Chain
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2)
)

while True:
    input_text = input("You: ")
    if input_text.strip() == 'exit':
        break
    response = conversation.predict(input=input_text)
    print(f"Bot: {response}")
    # response = conversation({"input": input_text}) print(f"Bot: {response}")
