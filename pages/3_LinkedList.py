import streamlit as st
from structures.linked_list import LinkedList

st.title("Linked List Visualizer")

if "linked_list" not in st.session_state:
    st.session_state.linked_list = LinkedList()

value = st.number_input("Enter an Integer", step=1)

col1, col2 = st.columns(2) # create two columns

with col1:
    if st.button("Push"):
        st.session_state.linked_list.add_node(value)

with col2:
    if st.button("Pop"):
        if st.session_state.linked_list:
            st.session_state.linked_list.delete_node()

st.subheader("Linked List")
numbers = st.session_state.linked_list.traverse_list()

for num in numbers:
    st.write(f"| {num} |")