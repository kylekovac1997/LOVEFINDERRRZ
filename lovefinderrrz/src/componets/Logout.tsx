import axios from "axios";
import { useNavigate } from "react-router-dom";

export function Logout() {
  const navigate = useNavigate();

  function handleLogout() {
    axios.post("/api/logout").then(() => {
      navigate("/");
    });
  }

  return <button onClick={handleLogout}>Logout</button>;
}
