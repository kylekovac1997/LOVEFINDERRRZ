import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router";
export function NewUser() {
  const [profilePicture, setProfilePicture] = useState<File | null>(null);
  const [interests, setInterests] = useState("");
  const [profileDescription, setProfileDescription] = useState("");
  const navigate = useNavigate();
  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData();
    data.append("profile_picture", profilePicture || "");
    data.append("interests", interests);
    data.append("profile_description", profileDescription);

    axios
      .post("/api/users", data)
      .then((response) => {
        console.log(response.data);
        navigate("/");
      })
      .catch((error) => {
        console.error(error);
      });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Profile Picture:
        <input
          type="file"
          accept="image/*"
          onChange={(event) =>
            setProfilePicture(event.target.files?.[0] || null)
          }
        />
      </label>
      <br />
      <label>
        Interests:
        <textarea
          value={interests}
          onChange={(event) => setInterests(event.target.value)}
        />
      </label>
      <br />
      <label>
        Profile Description:
        <textarea
          value={profileDescription}
          onChange={(event) => setProfileDescription(event.target.value)}
        />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}
