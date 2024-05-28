const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');
const submitBtn = document.querySelector('.submitBtn');
const content = document.getElementById('content');
let todos = [];
const TODOS_KEY = 'todos';

function submitAddTodo(event) {
    event.preventDefault();
    const todoText = content.value;
    const newTodo = {
        text: todoText,
        id: Date.now(),
    };

    todos.push(newTodo);
    content.value = '';
    paintTodo(newTodo);
    saveTodos();
}

function paintTodo(todoText) {
    const li = document.createElement('li');
    li.id = todoText.id;
    const span = document.createElement('span');
    const button = document.createElement('button');

    span.innerText = todoText.text;
    button.innerText = 'X';
    button.addEventListener('click', deleteTodo);

    li.appendChild(span);
    li.appendChild(button);
    todoList.appendChild(li);
}

function deleteTodo(event) {
    const li = event.target.parentElement;
    li.remove();
    todos = todos.filter((todoText) => todoText.id !== parseInt(li.id));
    saveTodos();
}

function saveTodos() {
    window.localStorage.setItem(TODOS_KEY, JSON.stringify(todos));
}

todoForm.addEventListener('submit', submitAddTodo);

let tempTodos = JSON.parse(window.localStorage.getItem(TODOS_KEY));
if (tempTodos !== null) {
    todos = tempTodos;
    todos.forEach((todoText) => {
        paintTodo(todoText);
    });
}
