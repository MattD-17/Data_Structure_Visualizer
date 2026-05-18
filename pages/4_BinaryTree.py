import streamlit as st
from structures.binary_tree import BinaryTree
from utils.visualizer import draw_binary_tree

st.title("Binary Tree Visualizer")

if "binary_tree" not in st.session_state:
    st.session_state.binary_tree = BinaryTree()

value = st.number_input("Enter an Integer", step=1)

col1, col2 = st.columns(2)

with col1:
    if st.button("Insert"):
        st.session_state.binary_tree.add_node(value)

#with col2:
#    if st.button("Remove"):
 #       if st.session_state.binary_tree:
  #          st.session_state.binary_tree.remove(value)


items = st.session_state.binary_tree.get_tree()
st.subheader("Binary Tree")
fig = draw_binary_tree(items, st.session_state.binary_tree.max_nodes)
st.plotly_chart(fig, width="stretch")
