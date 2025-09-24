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

  return (
    <form onSubmit={submit} style={{maxWidth:360}}>
      <h2>Sign in</h2>
      <input placeholder="username" value={user} onChange={e=>setUser(e.target.value)} /><br/>
      <input placeholder="password" type="password" value={pass} onChange={e=>setPass(e.target.value)} /><br/>
      <button type="submit">Sign in</button>
      {error && <div style={{color:"red"}}>{error}</div>}
    </form>
  );
}
