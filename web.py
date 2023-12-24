import streamlit as st
import function
todos = function.get_todos()
def Add_todo():
    pass



st.title("My Todo Web App")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a Todos:",
              placeholder="Add new Todo.......",
              on_change=Add_todo,
              key="new_todo")    













# st.write("this is my first web app")