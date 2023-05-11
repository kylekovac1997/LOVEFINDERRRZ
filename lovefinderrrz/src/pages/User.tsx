import axios from "axios";
import { useEffect, useState } from "react";

interface UserProps {
  username: string;
  firstname: string;
  userid: string;
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

  return (
    <>
      <div>
        {userDetails.map((user, index) => (
          <div key={index}>
            <p>{user.username}</p>
            <p>{user.userid}</p>
            <img
              src={`data:image/png;base64,${user.profile_picture}`}
              alt="{user.profile_picture}"
            />

            <p>{user.profile_description}</p>
          </div>
        ))}
      </div>
    </>
  );
};
