import styled from "styled-components";

interface NavBarTitleProps {
  text: string;
  emoji: string;
}

const Title = styled.h1`
  align-items: center;
  font-size: 40px;
  ()margin-right: 430px;
  position: relative;
  display: flex;
`;
const Emoji = styled.span`
  display: inline-block;
  transform: rotate(-25deg);
`;

export const NavBarTitle = ({ text, emoji }: NavBarTitleProps) => {
  return (
    <Title>
      <Emoji>{emoji}</Emoji>
      {text}
    </Title>
  );
};
