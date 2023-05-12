import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router";
import styled from "styled-components";
import portalGif from "../componets/images/portal.gif";

const PageContainer = styled.div`
  background-image: url(${portalGif});
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
`;

const FormContainer = styled.form`
  text-align: center;
  display: flex;
  flex-direction: column;
  max-width: 400px;
  margin-top: 150px;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 8px;
`;

const Label = styled.label`
  margin-bottom: 10px;
  font-weight: bold;
`;

const Input = styled.input`
  padding: 8px;
  margin-bottom: 10px;
`;

const TextArea = styled.textarea`
  padding: 8px;
  margin-bottom: 10px;
`;

const SubmitButton = styled.button`
  padding: 10px 20px;
  background-color: #fe2e64;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

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
    <PageContainer>
      <FormContainer onSubmit={handleSubmit}>
        <Label>
          Profile Picture:
          <Input
            type="file"
            accept="image/*"
            onChange={(event) =>
              setProfilePicture(event.target.files?.[0] || null)
            }
          />
        </Label>
        <Label>
          Interests:
          <TextArea
            value={interests}
            onChange={(event) => setInterests(event.target.value)}
          />
        </Label>
        <Label>
          Profile Description:
          <TextArea
            value={profileDescription}
            onChange={(event) => setProfileDescription(event.target.value)}
          />
        </Label>
        <SubmitButton type="submit">Submit</SubmitButton>
      </FormContainer>
    </PageContainer>
  );
}
