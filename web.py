import streamlit as st
import function
todos = function.get_todos()
def Add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    function.write_todos(todos)



st.title("My Todo Web App")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a Todos:",
              placeholder="Add new Todo.......",
              on_change=Add_todo,
              key="new_todo")    













# st.write("this is my first web app")