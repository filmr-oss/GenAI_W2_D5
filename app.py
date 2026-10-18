from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# 1. Load environment variables
load_dotenv()

# 2. Define the Chat Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 3. Create the Prompt Template with chat history placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher. Explain technical concepts in simple terms with analogies. Answer follow-up questions using the ongoing context."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}")
])

# 4. Output Parser
parser = StrOutputParser()

# 5. Build the Chain
chain = prompt | model | parser

# 6. Initialize in-memory conversation list
chat_history = []

print("--- GenAI Explainer with Memory & Streaming ---")
print("Type 'exit' or 'quit' to stop.\n")

# 7. Interactive Loop
while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
        
    if not user_input:
        continue

    print("\nAI: ", end="", flush=True)
    
    # Collect streamed chunks so we can save the full AI reply to history
    full_response = ""
    for chunk in chain.stream({
        "input": user_input,
        "chat_history": chat_history
    }):
        print(chunk, end="", flush=True)
        full_response += chunk
        
    print("\n" + "-" * 40 + "\n")

    # Update conversation history for the next turn
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=full_response))