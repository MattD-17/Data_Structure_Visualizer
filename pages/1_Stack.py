import streamlit as st

st.title("Stack Visualizer")

if "stack" not in st.session_state:
    st.session_state.stack = []

value = st.number_input("Enter an Integer", step=1)

col1, col2 = st.columns(2) # create two columns

with col1:
    if st.button("Push"):
        st.session_state.stack.append(int(value()))

with col2:
    if st.button("Pop"):
        if st.session_state.stack:
            st.session_state.stack.pop()

st.subheader("Stack")
for item in st.session_state.stack:
    st.write(f"|{item} |")                    