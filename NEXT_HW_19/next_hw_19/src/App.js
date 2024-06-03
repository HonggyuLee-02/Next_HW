import { useState } from 'react';
import './App.css';

function Header({ onChangeMode, children }) {
    return <h1 onClick={() => onChangeMode()}>{children}</h1>;
}

function Article({ title, content, deadline }) {
    console.log({ title, content, deadline });
    return (
        <article>
            <h2>{title}</h2>
            <div className="article-content">
                <p>{content}</p>
                <div className="article-deadline">
                    <strong>마감 기간: </strong>
                    {deadline}
                </div>
            </div>
        </article>
    );
}

function Nav({ onChangeMode, list }) {
    return (
        <nav>
            <ol>
                {list.map((item, i) => (
                    <li key={i} onClick={() => onChangeMode(item.id)}>
                        <div>{item.title}</div>
                        <div>
                            <small>{item.deadline}</small>
                        </div>
                    </li>
                ))}
            </ol>
        </nav>
    );
}

function Create({ onCreate }) {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [deadline, setDeadline] = useState('');

    const handleClick = () => {
        onCreate(title, content, deadline);
        setTitle('');
        setContent('');
        setDeadline('');
    };

    return (
        <div className="create-update-container">
            <p>
                <input type="text" placeholder="title" value={title} onChange={(e) => setTitle(e.target.value)}></input>
            </p>
            <p>
                <textarea placeholder="content" value={content} onChange={(e) => setContent(e.target.value)}></textarea>
            </p>
            <p>
                <input type="date" value={deadline} onChange={(e) => setDeadline(e.target.value)}></input>
            </p>
            <p>
                <button type="button" onClick={handleClick}>
                    생성
                </button>
            </p>
        </div>
    );
}

function Update({ onUpdate, item }) {
    const [title, setTitle] = useState(item.title);
    const [content, setContent] = useState(item.content);
    const [deadline, setDeadline] = useState(item.deadline);

    const handleClick = () => {
        onUpdate(title, content, deadline);
    };

    return (
        <div className="create-update-container">
            <p>
                <input type="text" placeholder="title" value={title} onChange={(e) => setTitle(e.target.value)}></input>
            </p>
            <p>
                <textarea placeholder="content" value={content} onChange={(e) => setContent(e.target.value)}></textarea>
            </p>
            <p>
                <input type="date" value={deadline} onChange={(e) => setDeadline(e.target.value)}></input>
            </p>
            <p>
                <button type="button" onClick={handleClick}>
                    수정
                </button>
            </p>
        </div>
    );
}

function App() {
    const [mode, setMode] = useState('HOME');
    const [id, setId] = useState(-1);
    const [list, setList] = useState([
        {
            id: 0,
            title: 'Operations reasearch',
            content: 'Team Project',
            deadline: '2023-06-10',
        },
        {
            id: 1,
            title: '회귀 분석 기말고사',
            content: 'ㅈㄱㄴ',
            deadline: '2023-06-20',
        },
        { id: 2, title: '6/8-9 무박해커톤', content: '이건 ㄹㅇ이다', deadline: '2023-06-08' },
    ]);

    let title;
    let content;
    let deadline;

    if (mode === 'HOME') {
        title = 'ToDoList';
        content = '무엇이든 즐겁게 하는 것이 가장 중요하다.';
        deadline = '';
    } else if (mode === 'READ') {
        const item = list.find((item) => item.id === id);
        if (item) {
            title = item.title;
            content = item.content;
            deadline = item.deadline;
        } else {
            title = '항목을 찾을 수 없음';
            content = '선택한 항목이 존재하지 않습니다.';
            deadline = '';
        }
    }

    const handleCreate = (title, content, deadline) => {
        const newItem = { id: list.length, title, content, deadline };
        setList([...list, newItem]);
        setId(newItem.id);
        setMode('READ');
    };

    const handleUpdate = (title, content, deadline) => {
        setList(list.map((item) => (item.id === id ? { ...item, title, content, deadline } : item)));
        setMode('READ');
    };

    const handleDelete = () => {
        setList(list.filter((item) => item.id !== id));
        setMode('HOME');
        setId(-1);
    };

    return (
        <div className="App">
            <Header onChangeMode={() => setMode('HOME')}>ToDoList</Header>
            <Nav
                list={list}
                onChangeMode={(_id) => {
                    setMode('READ');
                    setId(_id);
                }}
            ></Nav>
            <Article title={title} content={content} deadline={deadline}></Article>
            {mode === 'CREATE' && <Create onCreate={handleCreate} />}
            {mode === 'HOME' && <button onClick={() => setMode('CREATE')}>Create list</button>}
            {mode === 'READ' && (
                <>
                    <button onClick={() => setMode('UPDATE')}>revise the schedule!</button>
                    <button onClick={handleDelete}>It is done.</button>
                </>
            )}
            {mode === 'UPDATE' && <Update onUpdate={handleUpdate} item={list.find((item) => item.id === id)} />}
        </div>
    );
}

export default App;
