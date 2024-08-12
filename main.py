import streamlit as st
import random
import pandas as pd

if 'numbers' not in st.session_state:
    st.session_state.numbers = []

def generate_random_number():
    new_number = random.randint(1, 100)
    st.session_state.numbers.append(new_number)
    return new_number

def clear_data():
    st.session_state.numbers = []

st.title("Live Plot Generator")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Controls")
    if st.button("Generate Random Number"):
        num = generate_random_number()
        st.write(f"\t Random Number: {num}")
    # if st.button("Generate Random Number 2"):
    #     generate_random_number()
    # if st.button("Generate Random Number 3"):
    #     generate_random_number()
    
    if st.button("Clear Data"):
        clear_data()

with col2:
    st.header("Generated Numbers Plot")
    
    if st.session_state.numbers:
        numbers_df = pd.DataFrame(st.session_state.numbers, columns=["Random Numbers"])
        
        if len(st.session_state.numbers) == 1:
            st.write("Only one number generated, plotting as a point.")
            st.write(numbers_df)
        else:
            st.line_chart(numbers_df)
    else:
        st.write("No numbers generated yet.")
