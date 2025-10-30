import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state['input_todo'].strip().title()
    if new_todo == '':
        return
    st.session_state.todos.append(new_todo)
    functions.write_todos(st.session_state.todos)
    st.session_state.input_todo = ""


def remove_todo():
    for index, todo in enumerate(st.session_state.todos):
        if st.session_state['checkbox_'+todo]:
            st.session_state.todos.pop(index)
            functions.write_todos(st.session_state.todos)
            print(f"deleted {todo}")
            del st.session_state['checkbox_'+todo]


st.title('Todos')
if 'todos' not in st.session_state:
    st.session_state['todos'] = functions.get_todos()

for todo in st.session_state.todos:
    st.checkbox(todo, key='checkbox_'+todo, on_change=remove_todo)
st.text_input(label="  ", key="input_todo", placeholder="Type Todo", on_change=add_todo)
