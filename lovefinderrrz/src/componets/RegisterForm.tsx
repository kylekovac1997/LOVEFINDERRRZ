import { useState } from "react";
import { DialogFunction } from "./Dialog";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export function Registration() {
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [gender, setGender] = useState("");
  const [password, setPassword] = useState("");
  const [comfirmPassword, setComfirmPassword] = useState("");
  const navigate = useNavigate();

  async function handleRegistration(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (password === comfirmPassword) {
      const response = await axios.post("/api/register", {
        "first-name": firstName,
        "last-name": lastName,
        gender: gender,
        "date-of-birth": dateOfBirth,
        userName: username,
        email: email,
        phoneNumber: phone,
        Password: password,
      });
      if (response.status >= 0 && response.status < 500) {
        navigate("/NewUser");
      } else {
        alert("An error occurred while processing your registration.");
      }
    } else {
      setComfirmPassword("");
      alert("The passwords do not match. Please try again.");
    }
  }

  return (
    <>
      <DialogFunction buttonText={"Sign Up"} headerText={"Welcome"}>
        <form onSubmit={handleRegistration}>
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
            First Name:
            <input
              type="text"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
          </label>
          <br />
          <label>
            Last Name:
            <input
              type="text"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
          </label>
          <br />
          <label>
            Phone:
            <input
              type="text"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
            />
          </label>

          <br />
          <label>
            Email:
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </label>
          <br />
          <label>
            Date Of Birth:
            <input
              type="date"
              value={dateOfBirth}
              onChange={(e) => setDateOfBirth(e.target.value)}
            />
          </label>
          <br />
          <label>
            Gender:
            <select value={gender} onChange={(e) => setGender(e.target.value)}>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="trans">Trans</option>
              <option value="other">Other</option>
            </select>
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
          <br />
          <label>
            Comfirm Password:
            <input
              type="password"
              value={comfirmPassword}
              onChange={(e) => setComfirmPassword(e.target.value)}
            />
          </label>
          <br />
          <button type="submit">Submit</button>
        </form>
      </DialogFunction>
    </>
  );
}
