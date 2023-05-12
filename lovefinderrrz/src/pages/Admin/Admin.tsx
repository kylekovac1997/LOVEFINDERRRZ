import axios from "axios";
import { useEffect, useState } from "react";
import { AdminNavBarContainer } from "../../componets/AdminNavBar";
import {
  Interests,
  Details,
  MainInfo,
  Picture,
  Username,
  UserContainer,
} from "../../componets/ProfileStyleLayout";

interface AdminProps {
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

export function Admin() {
  const [adminDetails, setAdminDetails] = useState<AdminProps[]>([]);

  useEffect(() => {
    axios.get("/api/admin").then((response) => {
      setAdminDetails(response.data.admin);
    });
  }, []);

  return (
    <>
      <AdminNavBarContainer></AdminNavBarContainer>
      <h1>Admin Page</h1>

      <div>
        {adminDetails.map((user, index) => (
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
              {user.interests}
            </Interests>
          </UserContainer>
        ))}
      </div>
    </>
  );
}
