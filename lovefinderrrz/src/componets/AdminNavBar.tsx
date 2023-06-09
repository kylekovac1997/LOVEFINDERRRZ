import styled from "styled-components";
import { Container } from "./StyleContainer";
import { StyledAdminLink } from "./StyledNavLink";

const AdminNavBar = styled(Container)`
  background-color: #fe2e64;
  float: right;
  width: 120px;
  height: 989px;
`;

export const AdminNavBarContainer = () => {
  return (
    <>
      <AdminNavBar>
        <StyledAdminLink to="/FindUsers">Find Users</StyledAdminLink>
        <br />
        <StyledAdminLink to="/EditUsers">Edit Users</StyledAdminLink>
      </AdminNavBar>
    </>
  );
};
