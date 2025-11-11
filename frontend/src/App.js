import React, {useState} from "react";
import Login from "./components/Login";
import Patients from "./components/Patients";

export default function App(){
  const [token, setToken] = useState(null);

  if(!token) return React.createElement(Login, {onLogin: (t)=>setToken(t)});
  return React.createElement(
    'div',
    {style: {padding:20}},
    React.createElement('h1', null, 'TheoApp - Dashboard (Web)'),
    React.createElement(Patients, {token: token})
  );
}
