import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# 1. Load environment variables (.env)
load_dotenv()

# 2. Page Configuration
st.set_page_config(page_title="GenAI Concept Explainer", page_icon="🤖")
st.title("🤖 GenAI Concept Explainer")
st.caption("Ask any complex technical topic and get an easy-to-understand analogy!")

# 3. Setup LangChain Chain
@st.cache_resource
def get_chain():
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful teacher. Explain technical concepts in simple terms with analogies. Answer follow-up questions using the ongoing context."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])
    parser = StrOutputParser()
    return prompt | model | parser

chain = get_chain()

# 4. Initialize Chat History in Streamlit Session State
# Streamlit reruns the script on each user interaction, so session_state keeps memory alive
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Past Messages in the UI
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# 6. Handle New User Input
if user_prompt := st.chat_input("Enter a concept or ask a follow-up..."):
    # Display the user's message immediately
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Stream the AI's response in real-time
    with st.chat_message("assistant"):
        # We pass a generator of chunks to st.write_stream
        def generate_response():
            for chunk in chain.stream({
                "input": user_prompt,
                "chat_history": st.session_state.messages
            }):
                yield chunk

        full_reply = st.write_stream(generate_response())

    # Save to history for multi-turn context
    st.session_state.messages.append(HumanMessage(content=user_prompt))
    st.session_state.messages.append(AIMessage(content=full_reply))