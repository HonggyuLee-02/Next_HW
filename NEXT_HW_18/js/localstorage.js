const username = document.querySelector('.username');
const usernameWrapper = document.querySelector('.usernameWrapper');
const header = document.querySelector('#header');

function setUsername() {
    window.localStorage.setItem('username', username.value);
    username.value = '';
    checkUsername();
}

function checkUsername() {
    const checkName = window.localStorage.getItem('username');
    if (checkName) {
        usernameWrapper.style.display = 'none'; // 'style' should be lowercase
        header.innerHTML = `<h1>${window.localStorage.getItem(
            'username'
        )}의 To Do List</h1><button type="button" onclick="resetUsername()">초기화</button>`;
    } else {
        usernameWrapper.style.display = 'flex'; // 'style' should be lowercase
        header.innerHTML = ``;
    }
}
checkUsername();

function resetUsername() {
    window.localStorage.removeItem('username');
    checkUsername();
}
