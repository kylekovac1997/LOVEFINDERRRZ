import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import {
  Interests,
  Details,
  MainInfo,
  Picture,
  Username,
  UserContainer,
} from "../componets/ProfileStyleLayout";

interface UserProfileProps {
  userid: string;
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

export function UserProfile() {
  const { username } = useParams<{ username: string }>();
  const [userProfiles, setUserProfiles] = useState<UserProfileProps[]>([]);

  useEffect(() => {
    axios.get(`/api/UserProfiles/${username}`).then((response) => {
      setUserProfiles(response.data.users);
    });
  }, [username]);

  const handleLike = (userid: string) => {
    axios.post(`/api/liked/${userid}`);
    console.log(userid);
  };

  const handleDislike = (id: string) => {
    // Implement your logic for handling a dislike event
    console.log("Disliked user with id:", id);
  };

  return (
    <>
      {userProfiles.map((user, index) => (
        <div key={index}>
          <UserContainer key={index}>
            {" "}
            <Username>{user.username}</Username>
            <Picture
              src={`data:image/png;base64,${user.profile_picture}`}
              alt="{user.profile_picture}"
            ></Picture>
            <Details>
              {" "}
              <button onClick={() => handleLike(user.userid)}>Like</button>
              <button onClick={() => handleDislike(user.userid)}>X</button>
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
        </div>
      ))}
    </>
  );
}
