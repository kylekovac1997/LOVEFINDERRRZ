import styled from "styled-components";
import portalGif from "../componets/portal.gif";
interface ButtonProps {
  text: string;
  onClick: () => void;
}

const StyledButton = styled.button`
  background-image: url(${portalGif});
  background-color: transparent;
  border: none;
  background-size: cover;
  background-position: center;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  text-align: center;
  color: transparent;
  &:hover {
    color: white;
    font-weight: bold;
  }
`;

export const ProfileBtn: React.FC<ButtonProps> = ({ text, onClick }) => {
  return <StyledButton onClick={onClick}>{text}</StyledButton>;
};
