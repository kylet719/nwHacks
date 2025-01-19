import './App.css';
import { Routes, Route } from 'react-router-dom';
import Webcam from './pages/Webcam';
import SpotifyLogin from './pages/SpotifyLogin';

export default function Layout() {
  return (
    <div>
      <Routes>
        <Route exact path='/' element={<SpotifyLogin />} />
        <Route path='/webcam' element={<Webcam />} />
      </Routes>
    </div>
  );
}