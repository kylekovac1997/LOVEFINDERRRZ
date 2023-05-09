import styled from "styled-components";

interface ButtonProps {
  text: string;
  onClick: () => void;
}

const StyledButton = styled.button`
  background-color: white;
  color: black;
  padding: 10px 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  text-align: center;
`;

export const ProfileBtn: React.FC<ButtonProps> = ({ text, onClick }) => {
  return <StyledButton onClick={onClick}>{text}</StyledButton>;
};
