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

  return React.createElement(
    'div',
    null,
    React.createElement('h3', null, 'Patients'),
    React.createElement(
      'ul',
      null,
      patients.map(p=>
        React.createElement(
          'li',
          {key: p.id},
          p.first_name,
          ' ',
          p.last_name,
          ' — MRN: ',
          p.medical_record_number
        )
      )
    )
  );
}
