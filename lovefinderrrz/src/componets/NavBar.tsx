import { useNavigate } from "react-router";
import { ProfileBtn } from "./ProfileBtn";
import { NavBarContainer } from "./StyleContainer";
import { StyledLink } from "./StyledNavLink";
import { NavBarTitle } from "./NavBarTitle";
import { DialogFunction } from "./Dialog";
import { Logout } from "./Logout";
interface NavBarProps {
  isAdmin: boolean;
}

export const Navbar = ({ isAdmin }: NavBarProps) => {
  const navigate = useNavigate();
  sessionStorage.getItem("isAdmin");
  console.log(isAdmin);
  const handleClick = () => {
    if (isAdmin) {
      navigate("/Admin");
    } else {
      navigate("/User");
    }
  };

  return (
    <>
      <DialogFunction
        buttonText={"Logout"}
        headerText={"Are you sure you want to leave"}
      >
        <Logout></Logout>
      </DialogFunction>
      <NavBarContainer>
        <NavBarTitle emoji={" ❤️"} text={"LOVEFINDERRRZ"}></NavBarTitle>
        <StyledLink to="/Home">Home</StyledLink>
        <StyledLink to="/About">About</StyledLink>
        <ProfileBtn text="Profile" onClick={handleClick} />
      </NavBarContainer>
    </>
  );
};
