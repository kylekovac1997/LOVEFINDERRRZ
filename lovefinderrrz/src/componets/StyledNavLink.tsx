import { NavLink } from "react-router-dom";
import styled from "styled-components";

export const StyledLink = styled(NavLink)`
  color: #f2f2f2;
  text-decoration: none;
  margin: 0 1rem;
  font-size: 1.2rem;

  &:hover {
    color: #ccc;
  }

  &.active {
    color: #f0f0f0;
    font-weight: bold;
  }
`;

export const StyledAdminLink = styled(NavLink)`
  color: #f2f2f2;
  text-decoration: none;
  margin: 0 1rem;
  font-size: 1.2rem;
  float: right;
  &:hover {
    color: #ccc;
  }

  &.active {
    color: #f0f0f0;
    font-weight: bold;
  }
`;
