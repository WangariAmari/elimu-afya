import React, {useEffect, useState} from "react";
import axios from "axios";

export default function Patients({token}){
  const [patients,setPatients] = useState([]);

  useEffect(()=>{
    axios.get("http://localhost:8000/api/patients/", {
      headers: { Authorization: `Bearer ${token}` }
    }).then(res=>setPatients(res.data))
      .catch(err=>console.error(err));
  },[token]);

  return (
    <div>
      <h3>Patients</h3>
      <ul>
        {patients.map(p=>(
          <li key={p.id}>{p.first_name} {p.last_name} — MRN: {p.medical_record_number}</li>
        ))}
      </ul>
    </div>
  );
}
