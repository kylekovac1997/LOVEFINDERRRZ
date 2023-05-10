import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { DialogFunction } from "../componets/Dialog";

export function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    axios
      .post("/api/login", { username, password })
      .then((response) => {
        const data = response.data;
        if (data.is_admin) {
          sessionStorage.setItem("is_admin", "true");
          navigate("/Admin");
        } else {
          navigate("/User");
        }
      })
      .catch((error) => {
        console.error(error);
        alert("Invalid username or password. Please try again");
        setPassword("");
      });
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
          <br />
        </form>
      </DialogFunction>
    </>
  );
}

export default Login;
