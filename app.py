import streamlit as st 
import random


def restart_game():
    st.session_state.word = random.choice(words)    
    st.session_state.attempt=10
    st.session_state.guess_input = ""


top_left, top_right = st.columns([6,1])
with top_right:
    st.markdown("###")
    st.button("🔄 Restart", on_click=restart_game)

words= [ "python", "laptop", "window", "garden", "bottle",
        "orange", "travel", "flower", "animal", "friend",
        "silver", "yellow", "market", "forest", 
        "island","developer", "algorithm", "function", "variable", "inheritance"]


st.markdown(
    "<h1 style='text-align:center; color:#2E86C1;'>Welcome to the Word Guessing Game!</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h2 style='color:#117A65;'>You have 10 chances to guess the word correctly!</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='color:#8E44AD;'>Choose Word from list of words!</h3>",
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #e3f2fd, #fce4ec);
    }
    </style>
""", unsafe_allow_html=True)


if "word" not in st.session_state:
    st.session_state.word = random.choice(words)


if "attempt" not in st.session_state:
    st.session_state.attempt=10

if "guess_input" not in st.session_state:
    st.session_state.guess_input = ""


word_html = " ".join([f"<span style='background-color:#f0f2f6; padding:8px 12px;border-radius:10px; margin:5px; display:inline-block;'>{w}</span>" for w in words])
st.markdown(word_html, unsafe_allow_html=True)


guess_words = st.text_input("Make a Guess!", key= "guess_input")


col1, col2 = st.columns(2)
with col1:
    if st.button("Submit"):
        
        if st.session_state.attempt==0:
            st.info(f"Game Over!. Correct word was {st.session_state.word }")
        elif not guess_words:
            st.warning("Please enter a word!")
            
        else:
            guess_words = guess_words.lower()


            if guess_words ==  st.session_state.word:
                st.success(" 🎉 Congratulations you made correct guess!",icon="✅")
                st.session_state.attempt = 0

            elif guess_words not in words:
                st.session_state.attempt -=1
                st.warning(f"Please choose word from words list only. You have {st.session_state.attempt} attempts remaining.")
    
            else:
                st.session_state.attempt -=1
                st.error(f"Wrong!,You have {st.session_state.attempt} reamining")

                if st.session_state.attempt == 0:
                    st.info(f"Game Over! Correct word was: {st.session_state.word}")
    
        
def clear():
    st.session_state.guess_input =""

with col2:
    st.button("Clear", on_click=clear)
    

st.info(f"Remaining Attempts: {st.session_state.attempt}")