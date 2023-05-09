import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { DialogFunction } from "../componets/Dialog";

export function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const response = await axios.post("/api/login", { username, password });
    const data = response.data;
    console.log(data);
    if (data.is_admin) {
      sessionStorage.setItem("is_admin", "true");
      navigate("/Admin");
    } else {
      navigate("/User");
    }
  };

  return (
    <>
      <DialogFunction buttonText={"LOGIN"} headerText={"LOVEFINDERRRZ"}>
        <form onSubmit={handleSubmit}>
          <label>
            Username:
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </label>
          <br />
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>
          <button type="submit">Submit</button>
        </form>
      </DialogFunction>
    </>
  );
}

export default Login;
