import streamlit as st
import uuid
import bedrock
import mysql.connector


# Rest of your Streamlit code...

# Streamlit app
def main():
    st.title("Your Streamlit App")

    # Fetch data from the database
    data = fetch_data()

    # Display data in Streamlit
    st.write("User Prompts and AI Responses:")
    for row in data:
        st.write(f"User Prompt: {row[0]}")
        st.write(f"AI Response: {row[1]}")
        st.write("---")



# Initialize session state variables
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if "llm_app" not in st.session_state:
    st.session_state.llm_app = bedrock

if "llm_chain" not in st.session_state:
    st.session_state.llm_chain = bedrock.bedrock_chain()

if "questions" not in st.session_state:
    st.session_state.questions = []

if "answers" not in st.session_state:
    st.session_state.answers = []

if "input" not in st.session_state:
    st.session_state.input = ""

USER_ICON = "E:\\DOWNLOADS_NEW\\AI-cbot.png"
AI_ICON = "E:\\DOWNLOADS_NEW\\USER-CBOT.png"

def write_top_bar():
    col1, col2, col3 = st.columns([2, 10, 3])
    with col2:
        header = "Amazon Titan Chatbot-API"
        st.write(f"<h3 class='main-header'>{header}</h3>", unsafe_allow_html=True)
    with col3:
        clear = st.button("Clear Chat")
    if clear:
        st.session_state.questions = []
        st.session_state.answers = []
        st.session_state.input = ""
        bedrock.clear_memory(st.session_state.llm_chain)

    return clear

clear = write_top_bar()

if clear:
    st.session_state.questions = []
    st.session_state.answers = []
    st.session_state.input = ""
    bedrock.clear_memory(st.session_state.llm_chain)

def handle_input():
    input_text = st.session_state.input

    llm_chain = st.session_state.llm_chain
    chain = st.session_state.llm_app
    result, amount_of_tokens = chain.run_chain(llm_chain, input_text)
    question_with_id = {
        "question": input_text,
        "id": len(st.session_state.questions),
        "tokens": amount_of_tokens,
    }
    st.session_state.questions.append(question_with_id)

    st.session_state.answers.append(
        {"answer": result, "id": len(st.session_state.questions)}
    )
    st.session_state.input = ""

def write_user_message(md):
    col1, col2 = st.columns([1, 12])

    with col1:
        st.image(USER_ICON, use_column_width="always")
    with col2:
        st.container()
        st.warning(md["question"])
        st.write(f"Tokens used: {md['tokens']}")

def render_answer(answer):
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image(AI_ICON, use_column_width="always")
    with col2:
        st.container()
        st.info(answer["response"])

def write_chat_message(md):
    chat = st.container()
    with chat:
        render_answer(md["answer"])

with st.container():
    for i in range(min(len(st.session_state.get("questions", [])), len(st.session_state.get("answers", [])))):
        q = st.session_state.questions[i]
        a = st.session_state.answers[i]
        write_user_message(q)
        write_chat_message(a)

st.markdown("---")
input_text = st.text_input(
    "You are talking to an AI, ask any question.", key="input", on_change=handle_input
)