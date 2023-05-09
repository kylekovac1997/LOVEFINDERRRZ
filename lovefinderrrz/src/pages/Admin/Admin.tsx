import axios from "axios";
import { useEffect, useState } from "react";

interface AdminProps {
  username: string;
  email: String;
  firstname: string;
  lastname: string;
  userid: number;
}

export function Admin() {
  const [adminDetails, setAdminDetails] = useState<AdminProps[]>([]);

  useEffect(() => {
    axios.get("/api/admin").then((response) => {
      setAdminDetails(response.data.user);
    });
  }, []);

  return (
    <>
      <h1>Admin Page</h1>

      {adminDetails.map((info) => (
        <div key={info.userid}>
          <p>{info.username}</p>
          <p>{info.userid}</p>
          <p>{info.email}</p>
        </div>
      ))}
    </>
  );
}
