import axios from "axios";
import { useEffect, useState } from "react";
import {
  Interests,
  Details,
  MainInfo,
  Picture,
  Username,
  UserContainer,
} from "../componets/ProfileStyleLayout";
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

export const UserPage = () => {
  const [userDetails, setUserDetails] = useState<UserProps[]>([]);

  useEffect(() => {
    axios.get("/api/user").then((response) => {
      setUserDetails(response.data.users || []);
    });
  }, []);
  console.log(userDetails);

  const deactivateUser = () => {
    const deactivateButton = document.getElementById(
      "deactivate"
    ) as HTMLButtonElement;

    if (deactivateButton.textContent === "Deactivate") {
      axios.post("/api/deactivate");
      deactivateButton.textContent = "Reactivate";
      deactivateButton.style.backgroundColor = "red";
    } else if (deactivateButton.textContent === "Reactivate") {
      axios.post("/api/reactivate");
      deactivateButton.textContent = "Deactivate";
      deactivateButton.style.backgroundColor = "green";
    }
  };

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
              <button id="deactivate" onClick={deactivateUser}>
                {user.active === "true" ? "Deactivate" : "Reactivate"}
              </button>
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
};
