import React, {useState} from "react";
import axios from "axios";

export default function Login({onLogin}){
  const [user,setUser]=useState("");
  const [pass,setPass]=useState("");
  const [error,setError]=useState(null);

  const submit=async(e)=>{
    e.preventDefault();
    try{
      const res = await axios.post("http://localhost:8000/api/auth/token/", { username: user, password: pass });
      onLogin(res.data.access);
    }catch(err){
      setError("Login failed");
    }
  };

  return React.createElement(
    'form',
    {onSubmit: submit, style: {maxWidth:360}},
    React.createElement('h2', null, 'Sign in'),
    React.createElement('input', {
      placeholder: 'username',
      value: user,
      onChange: e=>setUser(e.target.value)
    }),
    React.createElement('br'),
    React.createElement('input', {
      placeholder: 'password',
      type: 'password',
      value: pass,
      onChange: e=>setPass(e.target.value)
    }),
    React.createElement('br'),
    React.createElement('button', {type: 'submit'}, 'Sign in'),
    error && React.createElement('div', {style: {color:"red"}}, error)
  );
}
