import axios from "axios";
import { useEffect, useState } from "react";
import styled from "styled-components";

interface UserProps {
  username: string;
  firstname: string;
  lastname: string;
  dateofbirth: string;
  email: string;
  interests: string;
  active: string;
  createon: string;
  gender: string;
  profile_description: string;
  profile_picture: string;
}

const UserContainer = styled.div`
  display: grid;
  grid-template-areas:
    "username main main main  "
    "picture main main main  "
    "details main main main  "
    "details interest interest interest  ";
  gap: 10px;
  background-color: #04b4b4;
  padding: 10px;
  align-items: center;
  margin-bottom: 20px;
`;

const Username = styled.h2`
  grid-area: username;
  text-align: center;
  text-decoration: underline;
`;

const Picture = styled.img`
  grid-area: picture;
  width: 200px;
  height: 200px;
`;

const MainInfo = styled.div`
  grid-area: main;
  grid-column-start: 2;
  grid-column-end: 3;
`;

const Details = styled.div`
  grid-area: details;
  grid-column-start: 1;
  grid-column-end: 7;
`;

const Interests = styled.ul`
  text-align: center;
  grid-area: interest;
  grid-column-start: 2;
  grid-column-end: 4;
  list-style-type: none;
`;

export const UserPage = () => {
  const [userDetails, setUserDetails] = useState<UserProps[]>([]);

  useEffect(() => {
    axios.get("/api/user").then((response) => {
      setUserDetails(response.data.users || []);
    });
  }, []);
  console.log(userDetails);
  return (
    <>
      <div>
        {userDetails.map((user, index) => (
          <UserContainer key={index}>
            {" "}
            <Username>{user.username}</Username>
            <Picture
              src={`data:image/png;base64,${user.profile_picture}`}
              alt="{user.profile_picture}"
            />
            <Details>
              <h4>UserInfo</h4>
              {user.firstname}
              <br />
              {user.lastname}
              <br />
              {user.dateofbirth}
              <br />
              {user.email}
              <br />
              {user.createon}
              <br />
              {user.active}
              <br />
              {user.gender}
              <br />
            </Details>
            <MainInfo>
              <h4 style={{ textAlign: "center" }}>UserInfo</h4>
              {user.profile_description}
            </MainInfo>
            <Interests>
              <h4 style={{ textAlign: "center" }}>INTEREST</h4>
              <ul>
                {user.interests.split(".").map((interest, index) => (
                  <p key={index}>{interest}</p>
                ))}
              </ul>
            </Interests>
          </UserContainer>
        ))}
      </div>
    </>
  );
};
