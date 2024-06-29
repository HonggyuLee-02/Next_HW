import './App.css';
import Header from './components/Header/Header';
import Main from './components/main/Main';
import About from './components/About/About';
import LibrarySearch from './components/librarySearch/LibrarySearch';
import { Routes, Route } from 'react-router-dom';

function App() {
    return (
        <div>
            <Header />
            <Routes>
                <Route path="/" element={<Main />} />
                <Route path="/about" element={<About />} />
                <Route path="/library" element={<LibrarySearch />} />
            </Routes>
        </div>
    );
}

export default App;
