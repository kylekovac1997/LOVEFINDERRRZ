import styled from "styled-components";

export const UserContainer = styled.div`
  display: grid;
  grid-template-areas:
    "username main main main  "
    "picture main main main  "
    "details main main main  "
    "details interest interest interest  ";
  gap: 10px;
  background-color: #04b4b4;
  padding: 10px;
  align-items: center;
  margin-bottom: 20px;
`;

export const Username = styled.h2`
  grid-area: username;
  text-align: center;
  text-decoration: underline;
`;

export const Picture = styled.img`
  grid-area: picture;
  width: 200px;
  height: 200px;
`;

export const MainInfo = styled.div`
  grid-area: main;
  grid-column-start: 2;
  grid-column-end: 3;
`;

export const Details = styled.div`
  grid-area: details;
  grid-column-start: 1;
  grid-column-end: 7;
`;

export const Interests = styled.div`
  text-align: center;
  grid-area: interest;
  grid-column-start: 2;
  grid-column-end: 4;
  list-style-type: none;
`;
