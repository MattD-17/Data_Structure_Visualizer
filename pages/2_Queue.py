import streamlit as st
from structures.queue import Queue
from utils.visualizer import draw_queue

st.title("Queue Visualizer")

if "queue" not in st.session_state:
    st.session_state.queue = Queue()

value = st.number_input("Enter an Integer", step=1)

col1, col2 = st.columns(2)

with col1:
    if st.button("Enqueue"):
        st.session_state.queue.enqueue(value)

with col2:
    if st.button("Dequeue"):
        if st.session_state.queue:
            st.session_state.queue.dequeue()

items = st.session_state.queue.get_items()

st.subheader("Queue")
fig = draw_queue(items, st.session_state.queue.max_size)
st.plotly_chart(fig, width="stretch")   