import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import portalGif from "../componets/images/portal.gif";
import portal from "../componets/sounds/PortalSound.mp3";

interface HomeProps {
  id: string;
  username: string;
  profile_picture: string;
}

export function Home() {
  const [userProfiles, setUserProfiles] = useState<HomeProps[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get("/api/home").then((response) => {
      setUserProfiles(response.data.users);
    });
  }, []);
  const portalSound = new Audio(portal);
  const handleUserClick = (username: string) => {
    portalSound.play();
    navigate(`/UserProfile/${username}`);
  };

  const UserContainer = styled.div`
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: flex-start;
  `;

  const TileContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    border: grey 2px solid;
    background-color: #04b4b4;
    max-width: 350px;
    gap: 20px;
    justify-content: flex-start;
    &:hover {
      background-color: transparent;
      background-image: url(${portalGif});
      background-repeat: no-repeat;
      background-size: cover;
      background-position: center;
    }
  `;

  const StyledImage = styled.img`
    width: 300px;
    height: 300px;
  `;

  const NameText = styled.p`
    text-align: center;
    font-weight: bold;
  `;

  return (
    <UserContainer>
      {userProfiles.map((user, index) => (
        <TileContainer
          key={index}
          onClick={() => handleUserClick(user.username)}
        >
          <NameText>{user.username}</NameText>
          <StyledImage src={`data:image/png;base64,${user.profile_picture}`} />
        </TileContainer>
      ))}
    </UserContainer>
  );
}
