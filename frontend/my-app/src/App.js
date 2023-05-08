import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './pages/home/Home';
import Applications from './pages/applications/Applications';

function App() {
  return (
    <Routes>
		<Route path='/home' element={<Home></Home>}></Route>
		<Route path='/' element={<Applications></Applications>}></Route>
	</Routes>
  );
}

export default App;
