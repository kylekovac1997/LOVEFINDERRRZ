import { AdminNavBarContainer } from "../../componets/AdminNavBar";

import { useState } from "react";
import axios from "axios";

export const FindUsers = () => {
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [gender, setGender] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  async function handleRegistration(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const response = await axios.post("/api/admin/searchUser", {
      search_username: username,
      search_firstname: firstName,
      search_lastname: lastName,
      search_mobile: phone,
      search_email: email,
      search_gender: gender,
      search_dob: dateOfBirth,
    });
    setSearchResults(response.data.results);
  }

  return (
    <>
      <AdminNavBarContainer></AdminNavBarContainer>
      <h1>Find Users</h1>
      <form onSubmit={handleRegistration}>
        <br />
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
        <button type="submit">Search</button>
      </form>
      <div>
        <h2>Search Results:</h2>
        <ul>
          {searchResults.map((result) => (
            <li key={result[0]}>
              User ID: {result[0]}
              <br />
              Username: {result[3]}
              <br />
              First Name: {result[11]}
              <br />
              Last Name: {result[12]}
              <br />
              Gender: {result[10]}
              <br />
              Date of Birth: {result[6]}
              <br />
              Email: {result[1]}
              <br />
              Phone: {result[9]}
              <br />
              <br></br>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
};
