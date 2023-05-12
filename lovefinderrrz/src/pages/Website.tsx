import { NavBarTitle } from "../componets/NavBarTitle";
import { Registration } from "../componets/RegisterForm";
import Login from "./Login";
import styled from "styled-components";

const WebsiteContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
`;

const Title = styled.h1`
  font-size: 24px;
  margin-bottom: 10px;
`;

const Description = styled.p`
  font-size: 16px;
  margin-bottom: 20px;
`;

const FormContainer = styled.div`
  display: flex;
  gap: 20px;
`;

export const Website = () => {
  return (
    <WebsiteContainer>
      <Title>
        Welcome to <NavBarTitle text={"LOVEFINDERRRZ"} emoji={"❤️"} />
      </Title>
      <Description>
        Find your perfect match and discover love with LoveFinderrrz.
      </Description>
      <FormContainer>
        <Login />
        <Registration />
      </FormContainer>
    </WebsiteContainer>
  );
};
