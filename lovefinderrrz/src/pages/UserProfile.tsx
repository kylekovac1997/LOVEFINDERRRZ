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
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [messageText, setMessageText] = useState("");

  useEffect(() => {
    axios.get(`/api/UserProfiles/${username}`).then((response) => {
      setUserProfiles(response.data.users);
    });
    axios.get("/api/user").then((response) => {
      setCurrentUser(response.data.users[0]);
    });
  }, [username]);

  const handleLike = (userid: string) => {
    console.log("Liked user with userid:", userid);
  };

  const handleDislike = (userid: string) => {
    console.log("Disliked user with userid:", userid);
  };

  const sendMessage = (senderId: string, recipientId: string) => {
    axios.post("/api/sendMessage", {
      sender_id: senderId,
      recipient_id: recipientId,
      content: messageText,
    });
  };

  return (
    <>
      {userProfiles.map((user, index) => (
        <div key={index}>
          <UserContainer key={index}>
            <Username>{user.username}</Username>
            <Picture
              src={`data:image/png;base64,${user.profile_picture}`}
              alt={user.profile_picture}
            ></Picture>
            <Details>
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
          <div>
            <input
              type="text"
              placeholder="Type your message"
              value={messageText}
              onChange={(e) => setMessageText(e.target.value)}
            />
            <button
              onClick={() => sendMessage(currentUser?.userid, user.userid)}
            >
              Send
            </button>
          </div>
        </div>
      ))}
    </>
  );
}
