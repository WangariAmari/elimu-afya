import React, {useState} from "react";
import Login from "./components/Login";
import Patients from "./components/Patients";

export default function App(){
  const [token, setToken] = useState(null);

  if(!token) return <Login onLogin={(t)=>setToken(t)} />
  return (
    <div style={{padding:20}}>
      <h1>TheoApp - Dashboard (Web)</h1>
      <Patients token={token} />
    </div>
  );
}
