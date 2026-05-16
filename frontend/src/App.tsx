import { Routes, Route } from 'react-router-dom'

import './App.css'
import Dashboard from './components/Dashboard'
import CodeToSpec from './components/CodeToSpec'
import SpecToCode from './components/SpecToCode'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/code-to-spec" element={<CodeToSpec />} />
      <Route path="/spec-to-code" element={<SpecToCode />} />
    </Routes>
  )
}

export default App
