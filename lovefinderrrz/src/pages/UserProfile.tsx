import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

interface UserProfileProps {
  id: string;
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
}

export function UserProfile() {
  const { username } = useParams<{ username: string }>();
  const [userProfiles, setUserProfiles] = useState<UserProfileProps[]>([]);

  useEffect(() => {
    axios.get(`/api/UserProfiles/${username}`).then((response) => {
      setUserProfiles(response.data.users);
    });
  }, [username]);

  const handleLike = (id: string) => {
    // Implement your logic for handling a like event
    console.log("Liked user with id:", id);
  };

  const handleDislike = (id: string) => {
    // Implement your logic for handling a dislike event
    console.log("Disliked user with id:", id);
  };

  return (
    <>
      {userProfiles.map((userProfile) => (
        <div key={userProfile.id}>
          <h2>{userProfile.username}</h2>
          <p>First Name: {userProfile.firstname}</p>
          <p>Last Name: {userProfile.lastname}</p>
          <p>Date of Birth: {userProfile.dateofbirth}</p>
          <p>Email: {userProfile.email}</p>
          <p>Interests: {userProfile.interests}</p>
          <p>Active: {userProfile.active}</p>
          <p>Created On: {userProfile.createon}</p>
          <p>Gender: {userProfile.gender}</p>
          <p>Profile Description: {userProfile.profile_description}</p>
          <button onClick={() => handleLike(userProfile.id)}>Like</button>
          <button onClick={() => handleDislike(userProfile.id)}>Dislike</button>
        </div>
      ))}
    </>
  );
}
