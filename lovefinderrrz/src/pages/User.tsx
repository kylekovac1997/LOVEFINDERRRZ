import axios from "axios";
import { useEffect, useState } from "react";

interface UserProps {
  username: string;
  userid: string;
}

export const UserPage = () => {
  const [userDetails, setUserDetails] = useState<UserProps[]>([]);

  useEffect(() => {
    axios.get("/api/user").then((response) => {
      setUserDetails(response.data.user);
    });
  });

  return (
    <>
      <div>
        {userDetails.map((user) => (
          <div key={user.userid}>
            <p>{user.username}</p>
            <p>{user.userid}</p>
          </div>
        ))}
      </div>
    </>
  );
};
