import { ReactNode, useState } from "react";
import portal from "./sounds/PortalSound.mp3";
import styled, { keyframes } from "styled-components";
import portalGif from "../componets/images/portal.gif";

interface DialogProps {
  buttonText: string;
  headerText: string;
  children: ReactNode;
}

const grow = keyframes`
  from {
    transform: scale(0);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
`;

const fadeIn = keyframes`
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
`;

const DialogContainer = styled.dialog`
  right: 50px;
  text-align: center;
  border: none;
  background-color: transparent;
  background-image: url(${portalGif});
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 700px;
  width: 700px;
  transform: scale(0);
  animation-name: ${grow};
  animation-duration: 0.9s;
  animation-delay: 0.6s;
  animation-fill-mode: forwards;

  > h2 {
    margin-top: 220px;
    opacity: 0;
    animation-name: ${fadeIn};
    animation-duration: 0.3s;
    animation-delay: 2s;
    animation-fill-mode: forwards;
  }

  > .dialog-children {
    font-size: large;
    opacity: 0;
    animation-name: ${fadeIn};
    animation-duration: 0.3s;
    animation-delay: 2s;
    animation-fill-mode: forwards;
  }

  > button {
    opacity: 0;
    animation-name: ${fadeIn};
    animation-duration: 0.3s;
    animation-delay: 2s;
    animation-fill-mode: forwards;
  }
`;
const LinkButton = styled.a`
  display: inline-block;
  font-size: 1em;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  color: #fff;
  background-color: none;
  border: none;
  cursor: pointer;
  &:hover {
    color: #444;
  }
`;

export const DialogFunction: React.FC<DialogProps> = ({
  buttonText,
  headerText,
  children,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const portalSound = new Audio(portal);
  const openDialog = () => {
    portalSound.play();
    setIsOpen(true);
    setTimeout(() => {}, 2000);
  };

  const closeDialog = () => {
    setIsOpen(false);
  };

  return (
    <>
      <LinkButton onClick={openDialog}>{buttonText}</LinkButton>
      <DialogContainer open={isOpen} onClose={closeDialog}>
        <h2>{headerText}</h2>
        <div className="dialog-children">{children}</div>
        <br />
        <button onClick={closeDialog}>X</button>
      </DialogContainer>
    </>
  );
};
